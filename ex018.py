anoNascimento = int(input("Em que ano você nasceu? "))
anoAtual = int(input("Em qual ano nós estamos? "))
idade = anoAtual - anoNascimento
if idade >= 18:
    print(f"Você tem {idade} anos, você pode votar.")
else:
    print(f"Você tem {idade} anos, você ainda não pode votar.")
