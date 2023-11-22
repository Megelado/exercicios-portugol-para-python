c = 1
soma = 0
ad = 0
peso90 = 0
levebaixo = 0
grandepesado = 0
while c <= 7:
    peso = float(input(f'Qual o peso da {c}° pessoa: '))
    if peso > 90:
        peso90 += 1
    altura = float(input('Qual a altura dela: '))
    if peso < 50 and altura < 1.6:
        levebaixo += 1
    if altura > 1.9 and peso > 100:
        grandepesado += 1
    soma = ad + altura
    ad = soma
    c += 1
media = soma / 7
print(f'A média de idade do grupo foi de {media} metros.')
if peso90 == 1:
    print('Há apenas uma pessoa que pesa mais de 90 kilos no grupo.')
else:
    if peso90 > 1:
        print(f'Há {peso90} pessoas que pesam mais de 90 kilos no grupo.')
    else:
        print('Não há pessoas que pesam mais de 90 kilos neste grupo.')
if levebaixo == 1:
    print('Há apenas uma pessoa que pesa menos de 50 kilos e mede menos de 1.60 metros.')
else:
    if levebaixo > 1:
        print('Há {} pessoas que pesam menos de 50 kilos e medem menos de 1.60 metros.')
    else:
        print('Não há pessoas que pesam menos de 50 kilos e medem menos de 1.60 metros.')
if grandepesado == 1:
    print('Há apenas uma pessoa que pesa mais de 100 kilos e mede mais de 1.90 metros neste grupo.')
else:
    if grandepesado > 1:
        print('Há {} pessoas que pesam mais de 100 kilos e medem mais de 1.90 neste grupo.')
    else:
        print('Não há pessoas que pesam mais de 100 kilos e medem mais de 1.90 metros neste grupo.')
