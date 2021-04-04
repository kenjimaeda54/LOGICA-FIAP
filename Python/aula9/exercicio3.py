numero1 = float(input("Entre com numero real "))
numero2 = float(input("Entre com outro numero real "))
numero3 = float(input("Entre com o terceiro numero real "))

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
