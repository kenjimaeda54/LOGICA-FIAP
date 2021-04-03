numeroConta = input("Qual numero da sua conta? ")

if( len(numeroConta) == 3  ):
    validar = numeroConta[2] + numeroConta[1] + numeroConta[0]
    soma = int(numeroConta) + int(validar) 
    converter = str(soma)
    primeiro = int(converter[0])*1
    segundo = int(converter[1])*2
    terceiro = int(converter[2])*3
    multiplicacao = primeiro + segundo + terceiro
    digito = str(multiplicacao)
    print("Tudo certo o digito da sua conta é ", digito[1])
   
else:
    print("Por favor sua conta tem quantidade de 3 numeros,confira novamente e digite")
    