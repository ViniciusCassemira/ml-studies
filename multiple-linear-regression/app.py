import numpy as np
from itertools import combinations # Utilizada para iterar com os valores mais abaixo

posicao_variavel_dependente_csv = 2 # price
posicao_variavel_independente_csv = [3, 4, 5] #[3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
quantidade_features = [2, 3]
nome_arquivo_csv = "house_data.csv"

# Essa função vai anotar em uma rquivo .txt qual foi o rmse(Raiz do Erro Quadrático Médio)
# 'caldulado' a partir de x features e também as salva nessea arquivo
def write_logs(rmse, nomes_features_usadas):
    nomes_features_usadas = nomes_features_usadas[1:] # Removendo o primeiro item (variável dependente)
    quantidade_feature_atual = len(nomes_features_usadas)

    with open(f"./logs/{quantidade_feature_atual}-features.txt", "a") as file:
        file.write(f"{nomes_features_usadas} - rmse: {rmse:.5f}\n")

# Essa função vai retornar o valor previsto de um registro existente no dataset, para calcular a precisão do algoritmo
def RealizandoPrevisao(array_dados_apartamento, array_beta):
    return array_dados_apartamento @ array_beta

# Essa função vai retornar a diferença real para cada previsão realizada
# calculando a diferença do valor real(presente no dataset) e o que o algoritmo de regressão 'previu'
def CalculandoDiferencaCadaPrevisao(y, y_chapeu):
    return y - y_chapeu

# Raiz do Erro Quadrático Médio (RMSE)
def CalculandoErroQuadratico(y, y_chapeu):
    rmse = np.sqrt(np.mean((y - y_chapeu)**2))

    return rmse

def UsandoCombinacao(array_posicao_features_csv, posicao_variavel_dependente_csv):
    
    print(array_posicao_features_csv)
    Y_chapeu = np.array([]) # Definindo vetor vazio para y^ (valores previstos)

    posicao_valores_utilizados_csv = np.insert(array_posicao_features_csv, 0, posicao_variavel_dependente_csv)

    # Armazenando em um array os nomes das variáveis(dependentes e independentes) que usaremos do dataset
    nomes_campos_utilizados_csv_dataset = np.genfromtxt(nome_arquivo_csv, delimiter=',', max_rows=1, dtype=str, usecols=posicao_valores_utilizados_csv)

    # Armazenar somente os valores que setamos no array de posicões
    array_dados_selecionados_csv = np.genfromtxt(nome_arquivo_csv, delimiter=',', skip_header=1, usecols=posicao_valores_utilizados_csv)

    # Separando a variável alvo (Y) e as variáveis preditoras (X)
    Y = array_dados_selecionados_csv[:, 0]
    X_features = array_dados_selecionados_csv[:, 1:]

    # Adicionar uma coluna de números "1" no início da matriz X
    # Isso represanta o beta_0 na equação (o valor base da casa se tudo fosse zero)
    numero_linhas_matriz_X_features = X_features.shape[0] # Conta o número de linhas do array para ser usado em seguida
    X = np.c_[np.ones(numero_linhas_matriz_X_features), X_features]

    # Aplicando a Equação Normal: Beta = (X.T * T)^-1 * X.T * Y
    X_T = X.T # Transposta de X
    array_beta = np.linalg.inv(X_T @ X) @ X_T @ Y # np.linealg.inv calcula a matriz inversa da matriz

    # Iterando com cada valor no dataset para calcular a previsão e o y^ com base nas variáveis(dependentes e independentes)
    for i, X in enumerate(X):
        
        resultado_previsao = RealizandoPrevisao(X, array_beta)
        
        Y_chapeu= np.append(Y_chapeu, resultado_previsao)

        diferenca_previsao_realizada = CalculandoDiferencaCadaPrevisao(Y[i],resultado_previsao)

    # Calculando Erro quadrático e printando ele em um log
    raiz_error_quadratico_medio = CalculandoErroQuadratico(Y, Y_chapeu)
    write_logs(raiz_error_quadratico_medio, nomes_campos_utilizados_csv_dataset)

for n in quantidade_features:
    for comb in combinations(posicao_variavel_independente_csv, n):
        UsandoCombinacao(comb, posicao_variavel_dependente_csv)    