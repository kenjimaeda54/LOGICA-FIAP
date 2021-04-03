numero1 = int(input("Entre com numero inteiro "))
numero2 = int(input("Entre com outro numero inteiro "))
numero3 = int(input("Entre com o tercieiro numero inteiro "))

if(numero1 > numero2 and numero1 > numero3 and numero2 > numero3):
    print(numero1, numero2, numero3)
elif(numero1 > numero2 and numero1 > numero3 and numero3 > numero2):
    print(numero1, numero3, numero2)
elif(numero2 > numero1 and numero2 > numero3 and numero3 > numero1):
    print(numero2, numero3, numero1)
elif(numero2 > numero1 and numero2 > numero3 and numero1 > numero3):
    print(numero2, numero1, numero3)
elif(numero1 > numero2):
    print(numero3, numero1, numero2)
elif(numero2 > numero1):
    print(numero3, numero2, numero1)
