nome = input("Qual o nome do aluno? ")
nota1 = float(input(f"Qual a primeira nota de {nome}: "))
nota2 = float(input(f"Qual a segunda nota de {nome}: "))
media = (nota1 + nota2) / 2
print(f"A media foi de {media} pontos.")
if media > 7:
    print(f"{nome} teve um bom aproveitamento!")
else:
    print(f"{nome} não teve um bom aproveitamento!")