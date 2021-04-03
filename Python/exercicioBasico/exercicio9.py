candidatoA = int(input("Quantos votos o candidato A recebeu? "))
candidatoB = int(input("Quantos votos o candidato B recebeu? "))
candidatoC = int(input("Quantos votos o candidato C recebeu? "))
brancos = int(input("Houve votos brancos? Se sim,quantos foram? "))
nulos = int(input("Houve votos nulos? Se sim,quantos foram? "))

eleitores = candidatoA+candidatoB+candidatoC+brancos+nulos
percentualA = (candidatoA/eleitores)*100
percentualB = (candidatoB/eleitores)*100
percentualC = (candidatoC/eleitores)*100
percentualBrancos = (brancos/eleitores)*100
percentuaolNulos = (nulos/eleitores)*100

print("\nPercentual de votos no candidato A foi aproximadamente %.0f" %percentualA,
      "porcento\npercentual de votos no candidato B foi aproximadametne %.0f" %percentualB,
      "porcento\npercentual de votos no candidato C foi aproxidamente %.0f" %percentualC,
      "porcento\npercentual de votos brancos foi aproximadamente %.0f" % percentualBrancos,
      "porcento\npercentual de votos nulos foram %.0f" %percentuaolNulos,"porcento")
