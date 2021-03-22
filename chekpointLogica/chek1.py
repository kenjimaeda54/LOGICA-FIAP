nome = input("Digite seu nome por favor ")
salario = float(input("Digite seu salario mensal por favor "))
vendidoFeminino = float(input("Qual valor você vendeu no setor feminino? "))
vendidoMasculino = float(input("Qual valor você vendeu no setor masculino? "))
vendidoInfantil = float(input("Qual valor você vendeu no setor infantil? "))
vendidoBeleza = float(input("Qual valor você vendeu no setor de beleza? "))

feminino = 0.02
masculino = 0.02
infantil = 0.04
beleza = 0.06

comissao = (feminino*vendidoFeminino)+(masculino*vendidoMasculino)+(infantil*vendidoInfantil)+(beleza*vendidoBeleza)
total = comissao + salario

print("Prezado: ", nome, "\nSeu salario fixo por mes é de %.2f "%salario,
      "reais e sua comissao referente o mês vigente foi calculado em %.2f"%comissao,
      "reais\n Total a receber %.2f "% total, "reais")
