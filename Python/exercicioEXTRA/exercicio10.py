opcao =  int(input("Por favor escolha sua opção 1 e somar 2 é raiz quadrada: "))

if(opcao == 1):
  print("Você selecinou somar dois numeros")  
  numero = input("Preciso pelo menos dois numeros para somar,separe com virgula: ")
  somaArray = numero.split(',') 
  resultado =  int(somaArray[0]) + int(somaArray[1])
  print("O resltado da soma: ",resultado)
if( opcao == 2 ):
  print(" Você sellecinou raiz quadrada ")  
  numero = float(input(" Digite apenas um numero para realizar a operação: "))
  resultado = numero*numero
  print("O resultado do quadrado:%.2F"%resultado)    
    
