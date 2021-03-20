Algoritmo "exercicio7"

Var
valor,juros,dias,novoValor: real


Inicio
escreva("Qual valor do boleto?")
leia(valor)
escreva("Qual em reais  do juros por dia?")
leia(juros)
escreva("Quantos dias esta atrasado?")
leia(dias)
novoValor := (valor+(valor*(juros/100))*dias)
escreva("Novo valor a pagar é :",novoValor,"reais")

Fimalgoritmo