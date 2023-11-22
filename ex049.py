c = 1
numPar = 0
while c <= 6:
    num = int(input(f'Digite o {c}° número: '))
    c += 1
    if num % 2 == 0:
        numPar += 1
if numPar == 1:
    print(f'Há {numPar} valor par.')
else:
    if numPar > 1:
        print(f'Há {numPar} valores pares.')
    else:
        print('Não há nenhum valor par!')
