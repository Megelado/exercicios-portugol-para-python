ud = 0
soma = 0
a1 = int(input('Qual o primeiro termo da P.A: '))
R = int(input('Qual a razão: '))
for i in range(a1, 11):
    an = a1 + (i - 1) * R
    print(an, end=' ')
    soma = an + ud
    ud = soma
print('')
print(f'A soma da P.A deu {soma}')
