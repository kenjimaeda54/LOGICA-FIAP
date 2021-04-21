contador = 0
idade = 0
print("Digite as 10 idades para calcular a media")

while(contador <= 10):
    print(contador, end='')
    amarzenar = float(input("- "))
    while(amarzenar < 0):
        print("Por favor a idade tem que ser superior a 0")
        print(contador, end='')
        amarzenar = float(input("- "))
    # contador e a soma precisa estar dentro do primeiro while e fora do escopo de condição,
    # se não constantemente efetua soma é o contador
    contador += 1
    idade += amarzenar
print("Media da soma das idades:", idade/10)
