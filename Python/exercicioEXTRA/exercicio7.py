nome= input("Por favor qual nome do aluno? ")
notas= input("Quais formam as tres notas do semestre ")
faltas = int(input("Digite os numeros faltas "))

arrayNotas = notas.split(',')

quantidadeAula=( 80*0.25 ) 

somaNotas= int(arrayNotas[0])+int(arrayNotas[1])+int(arrayNotas[2])
mediaNota = somaNotas/3

if( faltas > quantidadeAula ):
    print("O aluno foi reprovado por falta")
elif( mediaNota < 7 ):
    print("O aluno foi reprovado por media")
else:
    print(nome,"foi aprovado")            
