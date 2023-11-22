c = 6
soma = 0
while c <= 100:
    na = c
    ud = soma
    soma = na + ud
    if c == 100:
        print(c)
        c += 2
    else:
        print(f'{c} + ', end=' ')
        c += 2
print(f'A soma de todos os numeros foi {soma}')
