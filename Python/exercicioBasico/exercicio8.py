salario = float(input("Qual valor do seu salario? "))
despessas = float(input("Qual valor da sua despessa mensal? "))

renda = (salario-despessas)*12
milhonario = 1000000/renda

print("Você aproximadamente em %.0f" % milhonario, "anos vai ficar milhonario")
