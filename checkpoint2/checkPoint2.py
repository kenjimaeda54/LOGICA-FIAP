pratos = int(input("Quantos pratos foram consumidos? "))

if(pratos > 0):
    valor = float(input("Qual valor da conta?R$:"))
    if(valor > 0):
        cupom = input(
            "\nCliente possui cumpom?Caso sim digite S,caso não digite N. ")
        pegaCupom = cupom[0]
        if(pegaCupom.upper() == "S"):
            nomeCupom = input("\nQual nome do cupom? ")
            if (nomeCupom.upper() != "BORALA10" and nomeCupom.upper() != "BORALA05"):
                contador = 0
                sair = ''
                while (nomeCupom.upper() != "BORALA10" and contador < 2 and nomeCupom.upper() != "BORALA05"):
                    sair = input(
                        "Errou!Deseja continuar,S para sim ou N para não ")
                    pegarSair = sair[0]
                    if(pegarSair.upper() == "S"):
                        print(contador+2, "--", end="")
                        nomeCupom = input("")
                        contador += 1
                    else:
                        contador = 3
                else:
                    print(
                        "Não foi possivel localizar o cupom,inicia novamente é peça ao cliente cupom valido")
            if(nomeCupom.upper() == 'BORALA10'):
                print("Legal,cupom valido!Nome do cupom:", nomeCupom)
                visita = input(
                    "É a primeira visita?Caso sim S,caso não N,\nAtenção apenas utlizar S ou N! ")
                if(visita.upper() != "S"):
                    while(visita.upper() != "S" and visita.upper() != "N"):
                        visita = input(
                            "E  primeira visita?Caso sim S,caso não N,\nAtenção aapenas utilizar S ou N!")
                elif(visita.upper() == "S"):
                    pessoa = int(
                        input("\nEla esta sozinha?Se sim digite 0,se não digite numero de pessoas."))
                    if(pessoa != 0):
                        if (pratos > 3 and valor > 500):
                            descont = 0.25 * valor
                            result = valor - descont
                            breack = result/pessoa
                            print("------------")
                            print("Valor da nota fiscal:R$", valor)
                            print("Desconto na nota fiscal:R$:", descont)
                            print("\nValor total da nota com desconto:R$", result)
                            print("Numeros de pessoas:", pessoa)
                            print("Total por pessoa R$:%.2f" % breack)
                            print("--------------")
                        elif(pratos < 3 and valor > 500):
                            descont = 0.21 * valor
                            result = valor - descont
                            breack = result/pessoa
                            print("------------")
                            print("Valor da nota fiscal:R$", valor)
                            print("Desconto na nota fiscal:R$:", descont)
                            print("\nNumero de pessoas:", pessoa)
                            print(" Valor total da nota com desconto:R$", result)
                            print("Valor por pessoa R$:%.2f" % breack)
                            print("--------------")
                        else:
                            descont = 0.15 * valor
                            result = valor - descont
                            breack = result/pessoa
                            print("------------")
                            print("Valor da nota ficasl:R$", valor)
                            print("Desconto na nota fiscal:R$:", descont)
                            print("\nNumero de pessoas:", pessoa)
                            print(" Valor total da nota com desconto:R$", result)
                            print("Valor por pessoa R$:%.2f" % breack)
                            print("--------------")
                    elif(pratos > 3 and valor > 500):
                        descont = 0.20 * valor
                        result = valor - descont
                        print("------------")
                        print("Valor da nota fiscal:R$", valor)
                        print("Desconto na nota fiscal:R$:", descont)
                        print("\nValor total da nota com desconto:R$", result)
                        print("--------------")
                    elif (pratos < 3 and valor > 500):
                        descont = 0.16 * valor
                        result = valor - descont
                        print("------------")
                        print("Valor da nota fiscal:R$", valor)
                        print("Desconto na nota fiscal:R$:", descont)
                        print("\nValor total da nota com desconto:R$", result)
                        print("--------------")
                    else:
                        descont = 0.10 * valor
                        result = valor - descont
                        print("------------")
                        print("Valor da nota ficasl:R$", valor)
                        print("Desconto na nota fiscal:R$:", descont)
                        print("\nValor total da nota com desconto:R$", result)
                        print("--------------")
                else:
                    print("E a segunda vez")
            if(nomeCupom.upper() == 'BORALA05'):
                print("\nLegal,cupom valido!Nome do cupom:", nomeCupom)
                visita = input(
                    "É a primeira visita?Caso sim S,caso não N,\nAtenção apenas utlizar S ou N! ")
                if(visita.upper() != "S"):
                    while(visita.upper() != "S" and visita.upper() != "N"):
                        visita = input(
                            "E  primeira visita?Caso sim S,caso não N,\nAtenção aapenas utilizar S ou N!")
                    if(visita.upper() == "S"):
                        pessoa = int(
                            input("\nEla esta sozinha?Se sim digite 0,se não digite numero de pessoas."))
                        if(pessoa != 0):
                            if (pratos > 3 and valor > 500):
                                descont = 0.20 * valor
                                result = valor - descont
                                breack = result/pessoa
                                print("------------")
                                print("Valor da nota fiscal:R$", valor)
                                print("Desconto na nota fiscal:R$:", descont)
                                print(
                                    "\nValor total da nota com desconto:R$", result)
                                print("Numeros de pessoas:", pessoa)
                                print("Total por pessoa R$:%.2f" % breack)
                                print("--------------")
                            elif(pratos < 3 and valor > 500):
                                descont = 0.16 * valor
                                result = valor - descont
                                breack = result/pessoa
                                print("------------")
                                print("Valor da nota fiscal:R$", valor)
                                print("Desconto na nota fiscal:R$:", descont)
                                print("\nNumero de pessoas:", pessoa)
                                print(
                                    " Valor total da nota com desconto:R$", result)
                                print("Valor por pessoa R$:%.2f" % breack)
                                print("--------------")
                            else:
                                descont = 0.10 * valor
                                result = valor - descont
                                breack = result/pessoa
                                print("------------")
                                print("Valor da nota ficasl:R$", valor)
                                print("Desconto na nota fiscal:R$:", descont)
                                print("\nNumero de pessoas:", pessoa)
                                print(
                                    " Valor total da nota com desconto:R$", result)
                                print("Valor por pessoa R$:%.2f" % breack)
                                print("--------------")
                        elif(pratos > 3 and valor > 500):
                            descont = 0.20 * valor
                            result = valor - descont
                            print("------------")
                            print("Valor da nota fiscal:R$", valor)
                            print("Desconto na nota fiscal:R$:", descont)
                            print("\nValor total da nota com desconto:R$", result)
                            print("--------------")
                        elif(pratos < 3 and valor > 500):
                            descont = 0.16 * valor
                            result = valor - descont
                            print("------------")
                            print("Valor da nota fiscal:R$", valor)
                            print("Desconto na nota fiscal:R$:", descont)
                            print(" Valor total da nota com desconto:R$", result)
                            print("--------------")
                        else:
                            descont = 0.10 * valor
                            result = valor - descont
                            print("------------")
                            print("Valor da nota ficasl:R$", valor)
                            print("Desconto na nota fiscal:R$:", descont)
                            print(" Valor total da nota com desconto:R$", result)
                            print("--------------")
                    else:
                        print("E a segunda vez")

        else:
            visita = input(
                "É a primeira visita?Caso sim S,caso não N,\nAtenção apenas utlizar S ou N! ")
            if(visita.upper() != "S"):
                while(visita.upper() != "S" and visita.upper() != "N"):
                    visita = input(
                        "E  primeira visita?Caso sim S,caso não N,\nAtenção aapenas utilizar S ou N!")
            if(visita.upper() == "S"):
                pessoa = int(
                    input("\nEla esta sozinha?Se sim digite 0,se não digite numero de pessoas."))
                if(pessoa != 0):
                    if (pratos > 3 and valor > 500):
                        descont = 0.15 * valor
                        result = valor - descont
                        breack = result/pessoa
                        print("------------")
                        print("Valor da nota fiscal:R$", valor)
                        print("Desconto na nota fiscal:R$:", descont)
                        print(
                            "\nValor total da nota com desconto:R$", result)
                        print("Numeros de pessoas:", pessoa)
                        print("Total por pessoa R$:%.2f" % breack)
                        print("--------------")
                    elif(pratos < 3 and valor > 500):
                        descont = 0.11 * valor
                        result = valor - descont
                        breack = result/pessoa
                        print("------------")
                        print("Valor da nota fiscal:R$", valor)
                        print("Desconto na nota fiscal:R$:", descont)
                        print("\nNumero de pessoas:", pessoa)
                        print(
                            " Valor total da nota com desconto:R$", result)
                        print("Valor por pessoa R$:%.2f" % breack)
                        print("--------------")
                    else:
                        descont = 0.5 * valor
                        result = valor - descont
                        breack = result/pessoa
                        print("------------")
                        print("Valor da nota ficasl:R$", valor)
                        print("Desconto na nota fiscal:R$:", descont)
                        print("\nNumero de pessoas:", pessoa)
                        print(
                            " Valor total da nota com desconto:R$", result)
                        print("Valor por pessoa R$:%.2f" % breack)
                        print("--------------")
                elif(pratos > 3 and valor > 500):
                    descont = 0.10 * valor
                    result = valor - descont
                    print("------------")
                    print("Valor da nota fiscal:R$", valor)
                    print("Desconto na nota fiscal:R$:", descont)
                    print("\nValor total da nota com desconto:R$", result)
                    print("--------------")
                elif(pratos < 3 and valor > 500):
                    descont = 0.6 * valor
                    result = valor - descont
                    print("------------")
                    print("Valor da nota fiscal:R$", valor)
                    print("Desconto na nota fiscal:R$:", descont)
                    print(" Valor total da nota com desconto:R$", result)
                    print("--------------")
                else:
                    print("Não possui direito aa desconto")

    else:
        print("Valor do prato tem que ser acioma de R$0,00")

else:
    print("Quantidade de pratos tem que ser acima de 0")
