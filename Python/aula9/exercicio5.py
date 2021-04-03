numero1 = int(input("Digite um numero inteiro "))
numero2 = int(input("Digite outro numero inteiro "))
numero3 = int(input("Digite o ultimo numero inteiro "))

if(numero3 > numero2 and numero3 > numero1 and numero2 > numero1 ):
  print("Parabéns. Os numeros foram digitados em ordem crescente")
else:
    print("Os numeros não estão em ordem crescente")
