## Some notes about logistic regression

É um algoritmo de classificação muito utilizado em Machine Learning e Estatística. Ela é usada para prever a probabilidade de um evento pertencer a uma determinada classe. O caso mais comum é a classificação binária, onde o resultado pode ser apenas duas opções (ex: "Sim/Não", "Spam/Não Spam", "Doente/Saudável", que mapeamos matematicamente como 1 ou 0).

Na regressão linear, tentamos prever um valor através da reta `𝑧 = 𝛽𝑇 ∙ 𝑥`. 
O problema de usar essa equação para classificar é que o resultado de `z` pode assumir qualquer valor entre infinito positivo e infinito negativo. Para o caso da classficação, precisamos de um resultado que esteja entre 0 e 1.

Para encaixar o valor da previsão nesse intervalo de tempo, a regressão logística passa sua saída linear por uma função matemática chamada função Sigmoide.

Afim de treinar o modelo medir a precisão das nossas previsões, usamos o Erro Quadrado Médio(MSE) na regressão linear. Na logística, utilizamos a função de Log Loss(Entropia Cruzada Binária)

## Termos

`decision boundary`: Se trata de um limiar de decisão, usado para classificar(tomar uma decisão final) um resultado. O mais comum é 0.5
**Exemplo**: 
- Se ŷ >= 0.5 -> o classificamos para a classe 1
- Se ŷ < 0.5 -> o classificamos para a classe 0

`Gradiente descendente` (Otimização): O objetivo do treinamento é encontrar valores do beta (𝛽) que diminuam a função de custo, sendo o gradiente descendente o método tradicional a ser usado.

Sendo o motor que faz o modelo 'aprender'. 

`learning rate`: É o tamanho do passo que você dá a cada atualização dos pesos. Se a taxa for alta, você pode 'passar batido' por pontos mais baixos, sem conseguir encontrar o peso ideal. Se for baixa, terá muita precisão, porém demorará muito tempo, provavelmente mais do que o necessário.

`Épocas`: É quando um algoritmo passa pelo conjunto de dados inteiro uma vez. Ao final de cada época, o gradiente é calculado e os pesos (𝛽) modificados. Se você diminuir a Taxa de Aprendizagem para ter mais precisão, geralmente precisará aumentar o número de Épocas para dar tempo ao modelo de chegar ao resultado esperado.