c = 500
soma = 0
while c >= 0:
    na = c
    ud = soma
    soma = na + ud
    if c == 0:
        print(c)
        c -= 50
    else:
        print(f'{c} + ', end=' ')
        c -= 50
print(f'A soma de todos os numeros foi {soma}')

