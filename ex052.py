c = 1
ud = 0
soma = 0
maidezoito = 0
mencin = 0
maior = 0
while c <= 8:
    idade = int(input(f'Qual a idade da {c}° pessoa: '))
    if idade > 18:
        maidezoito += 1
    if idade < 5:
        mencin += 1
    if idade > maior:
        maior = idade
    na = idade
    soma = ud + na
    ud = soma
    c += 1
media = soma / 8
print(f'A média do grupo foi {round(media, 2)} anos.')
if maidezoito == 0:
    print('Não há nenhuma pessoa com idade acima de 18.')
else:
    if maidezoito == 1:
        print('Há apenas uma pessoa com idade acima de 18.')
    else:
        print(f'Há {maidezoito} pessoas com idade acima de 18.')
if mencin == 0:
    print('Não há nenhuma pessoa com idade acima de 18.')
else:
    if mencin == 1:
        print('Há apenas uma pessoa com idade abaixo de 5.')
    else:
        print(f'Há {mencin} pessoas com idade abaixo de 5.')
print(f'A maior idade foi {maior} anos.')
