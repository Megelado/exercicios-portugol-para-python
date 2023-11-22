salAtual = float(input("Qual o salário? "))
sexo = input("Qual o sexo? ")
anosTrabalho = int(input("Quantos anos trabalha aqui? "))
novoSal = 0
if sexo.upper() == "F":
    if anosTrabalho < 15:
        novoSal = salAtual + (salAtual * 5 / 100)
    else:
        if 15 == anosTrabalho < 20:
            novoSal = salAtual + (salAtual * 12 / 100)
        else:
            novoSal = salAtual + (salAtual * 23 / 100)
if sexo.upper() == "M":
    if anosTrabalho < 20:
        novoSal = salAtual + (salAtual * 3 / 100)
    else:
        if 20 == anosTrabalho < 30:
            novoSal = salAtual + (salAtual * 13 / 100)
        else:
            novoSal = salAtual + (salAtual * 25 / 100)

print(f"O seu novo salário será de R${novoSal}")
