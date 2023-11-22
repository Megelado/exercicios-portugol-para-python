import random

acicin = 0
divtre = 0
c = 1
print('Os números sorteados foram: ')
while c <= 20:
    sort = random.randint(0, 10)
    c += 1
    if sort > 5:
        acicin += 1
    if sort % 3 == 0:
        divtre += 1
    print(sort, end=' ')
print('')
if acicin == 0:
    print('Não há nenhum valor acima de cinco.')
else:
    if acicin == 1:
        print('Há apenas um valor acima de cinco')
    else:
        print(f'Há {acicin} valores acima de cinco.')
if divtre == 0:
    print('Não há nenhum valor divisível por três.')
else:
    if divtre == 1:
        print('Há apenas um valor divisível por três.')
    else:
        print(f'Há {divtre} valores divisíveis por três.')
