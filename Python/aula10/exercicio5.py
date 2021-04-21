numero1 = int(input("Por favor insira numero inteiro "))
numero2 = int(input("Por favor insira outro numero inteiro "))
resultado = 0


if (numero1 < numero2):
    for contador in range(numero1+1, numero2):
        resultado += contador
    print("[", resultado, "]", end="")

if (numero2 < numero1):
    for contador in range(numero2+1, numero1):
        resultado += contador
    print("[", resultado, "]", end="")
