numero_1 = int(input("Digite numero inteiro "))
numero_2 = int(input("Digite numero inteiro "))


resultado = ((numero_1 % 2)*3)+(13-2+numero_2)

print("Restuldado da expressão é",resultado)
if(resultado <= 0):
    print("Resultado menor ou igual a zero")
elif((resultado > 0) and  (resultado <=20)):
    print("Resultado maior que zero e menor ou igual a 20")
else:
    print("Resutlado mairo que 20")  
    