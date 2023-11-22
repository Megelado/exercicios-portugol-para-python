def Media(n1, n2):
    notamedia = (n1 + n2) / 2
    return notamedia

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print(Media(nota1, nota2))
print(f'Amédia entre {nota1} e {nota2} é {Media(nota1, nota2)}')
