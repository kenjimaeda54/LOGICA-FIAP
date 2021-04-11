numero = int(input("Digite numero inteiro por favor entre 0 e 79: "))

if( numero > 0  ):
  if( numero <= 30):
    print("Numero esta entre 0 e 30")
  elif( numero >= 40 and numero <= 79 ):
     print("Numero esta entre 40 e 79")
  else:
      print( "Seu numero esta fora dos limites estabelecidos" )   
else:
    print(" seu numero e menor que 0 ")
