nomeCupom = input("Por favor digite o nome do cupom:")

# PRIMEIRO ELE VERIFICA  A CONDIAÇÃO SE A CONDIÇÃO E VERDADEIRA ELE ENTRA WHILE
# SE A CONDIÇÃO E FALSA SAI DO WHILE
if (nomeCupom != "BORALA10"):
    contador = 0
    checkCupom = input("Cupom invalido, você tem 3 chances: ")
    sair = ''
    while (checkCupom != "BORALA10" and contador < 2):
        sair = input(
            "Deseja continuar você errou novamente,S para sim ou N para não")

        if(sair[0] == "S"):
            print(contador+2, "--", end="")
            checkCupom = input("")
            contador += 1
        else:
            contador = 3

    if(checkCupom == "BORALA10"):
        print("eu achei")
    else:
        print("Eu não achei")
else:
    print("Eu achei")
