# Regressão Logística - Matriz de Confusão
Notas da aula do dia 07/04/2026 

#### Matriz de confusão:
|   | Previsão: Negativo  | Previsão: Positivo  |
|---|---|---|
| **Real: Negativo**  | Verdadeiro Negativo (VN)  | Falso Positivo (FP)  |
| **Real: Positivo**  | Falso Negativo (FN)  | Verdadeiro Positivo (VP)  |

`Acurácia`: _(VP + VN) / (VP + VN + FP + FN)_

`Precisão`: _VP / (VP + FP)_

`Revocação`: _VP / (VP + FN)_

`F-measure`: _(precisão * revocação) / ( precisão + revocação )_