compra= float(input("Digite o valor da compra R$ "))

if( compra < 20 ):
    valor =((compra * 0.45) + compra )
    print("Você precisa vender por R$%.2f"%valor,"para atingir 45 por cento de lucro")
if( compra >= 20  ):
    valor = (( compra * 0.30) + compra)    
    print("Você precisa vender por R$%.2f"%valor,"para atingir 30 por cento de lucro")