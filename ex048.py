c = 1
ud = 0
soma = 0
while c <= 7:
    num = int(input(f'Digite o {c}° número: '))
    an = num
    soma = an + ud
    ud = soma
    c += 1
print(soma)
