ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "É bissexto.")
else:
    print(ano, "Não é bissexto")
