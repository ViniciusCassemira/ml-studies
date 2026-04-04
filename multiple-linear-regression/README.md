# Multiple Linear Regression

Esse script tem como foco calcular a regressão linear múltipla de um dataset armazenado em um arquivo csv. 

### Estrutura do repositório
Aualmente, o repositório possui a seguinte estrutura:
```
multiple-linear-regression/
│
├── app.py
├── house_data.csv
│
├── logs/
│
├── README.md
└── regressao_multipla.ipynb
```
- `app.py`: Script (sem nenhum comentário)
- `house_data.csv`: Dataset utilizado como base e exemplo 
- `logs/`: Aonde serão armazenados os logs gerados pelo script (apague o seu conteúdo antes de utilizar o script)
- `regressao_multipla.ipynb`: Arquivo do Jupyter Notebook explicando o funcionamento do script 

### Fluxo de como funciona o algoritmo:
0. Setamos o dataset .csv via variável, junto com a posição da variável dependente, das independentes e as quantidades de features a testar.
1. Definir a posição das colunas no dataset que serão usadas (variável dependente e variáveis independentes).
2. Definir as quantidades de features que serão utilizadas nas combinações (ex: [2, 3] significa que o algoritmo vai testar combinações de 2 e depois de 3 variáveis independentes).
3. Criar um for duplo: o primeiro itera sobre as quantidades de features definidas no passo 2, o segundo itera sobre todas as combinações possíveis das colunas independentes com aquela quantidade.
- Para cada combinação de variáveis (ex: x1 e x2), carregar os dados do CSV e separar Y (variável dependente) e X (variáveis independentes).
- Adicionar uma coluna de 1s em X para representar o intercepto (β₀) na equação.
- Calcular os coeficientes usando a Equação Normal: β = (XᵀX)⁻¹ · Xᵀ · Y
- Iterar sobre cada registro do dataset, calcular o valor previsto (ŷ) e armazená-lo no array Y_chapeu.
- Calcular o RMSE (Raiz do Erro Quadrático Médio) comparando os valores previstos (ŷ) com os valores reais (Y).
- Salvar o RMSE e os nomes das features utilizadas em um arquivo de log separado por quantidade de features (ex: 2-features.txt).

### Funcionalidades
- [X] Calculando RMSE a partir de features e base de dados (detaset)
- [x] Salvando resultados obtidos em arquivos de log
- [ ] Remoção automática dos campos do tipo string de um dataset antes de realizar o cálculo da regressão
- [ ] Tratamento de erros básico
- [ ] Arquivos de log com formato compatível com o pandas 
- [ ] Verificação de variáveis incorretas