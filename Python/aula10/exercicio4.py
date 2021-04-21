numero1 = float(input("Coloque numero "))
numero2 = float(input("Coloque outro numero "))


converterNumero1 = int(numero1)
converterNumero2 = int(numero2)

if (numero1 < numero2):
    for contador in range(converterNumero1+1, converterNumero2+1):
        if(contador % 2 != 0):
            print("[", contador, "]", end="")

else:
    for contador in range(converterNumero2+1, converterNumero1+1):
        if(contador % 2 != 0):
            print("[", contador, "]", end="")
