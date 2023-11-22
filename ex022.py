anoNascimento = int(input("Em qual ano voce nasceu? "))
anoAtual = int(input("Em qual ano nós estamos? "))
idade = anoAtual - anoNascimento
if idade > 18:
    print(f"Já se passaram {idade-18} anos desde a idade ideal de alistamento.")
else:
   print(f"Ainda faltam {18 - idade} anos para você poder se alistar.")
