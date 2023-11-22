nome = input("Qual o nome do funcionário? ")
salario = float(input("Quanto ele ganha por mês? "))
anosTrabalho = int(input("Quantos anos ele trabalha nesta empresa? "))
if anosTrabalho <= 3:
    novoSalario = salario + (salario * 3 / 100)
else:
    if 3 < anosTrabalho < 10:
        novoSalario = salario + (salario * 12.5 / 100)
    else:
        novoSalario = salario + (salario * 20 / 100)
print(novoSalario)
