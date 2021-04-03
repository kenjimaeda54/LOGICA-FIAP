laboratorio = float(input("Qual nota do aluno no exame de laboratorio? "))
semestral = float(input("Qual valor da nota do aluno na avaliação semestral? "))
final = float(input("Qual valor da nota do exame final do aluno? "))

media = ((laboratorio*2)+(semestral*3)+(final*5))/10 

print("Valor da media ponderada ",media)

if(media >= 8 ):
    print("Conceito A")
elif(media >= 7):
    print("Conceito B")
elif(media >= 6):
    print("Conceito C")
elif(media >= 5 ):
    print("Conceito D") 
else:
    print("Conceito E")               