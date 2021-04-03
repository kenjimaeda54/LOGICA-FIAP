valor = float(input("Qual valor do boleto? "))
juros = float(input("Qual o percentual de juros? "))
dias = float(input("Quantos dias estao atrasado? "))


novoValor = (valor+(valor*(juros/100)))*dias

print("Novo valor do boleto é R$ %.2f" % novoValor)
