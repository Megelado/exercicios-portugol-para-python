idade = [1, 2, 3, 4, 5, 6, 7, 8]
c = 1
ud = 0
soma = 0
maior = 0
for i in range(0, 8):
    idade[i] = int(input(f'Digite a {c}° idade: '))
    if idade[i] > maior:
        maior = idade[i]
        posmai = i
    soma = ud + idade[i]
    ud = soma
    c += 1
med = soma / 8
print(f'A média de idade do grupo foi {med} anos.')
for i in range(0, 8):
    if idade[i] > 25:
        print(f'Temos uma idade maior que 25 anos na posição {i}.')
print(f'A maior idade digitada foi {maior} anos.')
print(f'A maior idade está na posição {posmai}')
