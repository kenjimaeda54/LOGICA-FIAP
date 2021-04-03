destino = input("Qual destino senhor deseja?\nPor favor,inicia a primeira letra com maisculo\nPossuimos,Nordeste,Norte,Centro-Oeste? ")
comprimento = len(destino)
viagemIdaVolta = input("Senhor deseja ida e volta?Digite S(sim) ou N(não) ")[0]
segundo = destino[2]
primeira = destino[0]
condicao = destino[comprimento - 5]
if((primeira == "N" or primeira== "C" or primeira=="N") 
    and (segundo == "r"  or segundo=="n") 
    and (condicao == "d" or condicao == "N" or condicao=="o" )  ):
     if(primeira == "N"  and  segundo =="r" and condicao== "N" ):
         if(viagemIdaVolta == "S" or viagemIdaVolta == "s"):
            print("Tudo certo o valor de ida e volta para Norte é R$400,00")
         else:
            print("Tudo certo o valor de ida para Norte é R$200,00")
     if(primeira == "N"  and segundo=="r" and condicao=="d"  ):
         if(viagemIdaVolta == "S" or viagemIdaVolta == "s"):
           print("Tudo certo o valor de ida e volta para Nordeste é R$628,00")
         else:
           print("Tudo certo o valor de ida para Nordeste é R$380,00")
     if(primeira == "C" and segundo=="n" and condicao=="o" ):
         if(viagemIdaVolta == "S" or viagemIdaVolta == "s"):
           print("Tudo certo o valor de ida e volta para Centro-Oeste é R$1100,00")
         else:
           print("Tudo certo o valor de ida para Centro-Oeste é R$620,00")   
else:
    print("Por favor verifique esta com maisculo a primeira letra\nCaso estiver,desculpe não realizamos viagem para este destino")