valor = float(input("Qual o preço da casa que deseja comprar? "))
salario = float(input("Qual o salário? "))
anos = int(input("Em quantos anos deseja terminar de pagar? "))
salacima30 = salario * 30/100
mes = anos*12
pm = valor / mes
if pm < salacima30:
    print("Seu empréstimo foi aprovado.")
else:
    print("Seu empréstimo foi recusado.")
