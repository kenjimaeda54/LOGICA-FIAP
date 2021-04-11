ladoA = float(input("Digite valor "))
ladoB = float(input("Por favor outro valor "))
ladoC = float(input("Digite o ultimo "))

sub = ladoB - ladoC
sub1 = ladoA - ladoC
sub2 = ladoA - ladoB

soma = ladoB + ladoC
soma1 = ladoA + ladoC
soma2 = ladoA + ladoB

if((sub < ladoA < soma) or (sub1 < ladoB < soma1) or (sub2 < ladoC < soma2)):
  print("Estes numeros podem formar  triangulo")
  if ((ladoA != ladoC != ladoB) and (ladoC != ladoB != ladoA)):
     print("Posivelmente seu triangulo é escaleno")

  elif (ladoA == ladoC == ladoB ):
      print("Posivelmente seu triangulo é equilatero")
     
  else:
      print("Posivelmente seu triangulo é isoceles")
else:
   print("Estes numeros não corresponde aos lados de triangulo")          
