salario = float(input("Coloque seu salario bruto, por favor R$ "))
condicao = False


resultado = 0.3*salario


if (salario <= 0  ):
    print("Por favor coloque salario acima de R$0.0")
else:
    condicao= True

if (condicao == True):
    prestacao = float(input("Qual  valor da prestação R$: "))
    condicao = False   
    if (prestacao <= 0):
           print("Por favor o valor da prestação precisa ser acima de R$0.00")    
    elif(prestacao >= resultado): 
           print("Sua prestação esta acima de 30% do seu salario bruto,coloque outro valor")
    else:
        print("Tudo certo parabéns seu emprestimo foi aceito")
    
    