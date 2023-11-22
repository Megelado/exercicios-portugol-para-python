ud = 0
soma = 0
c = 1
menor = None
while True:
    num = int(input('Escreva um número: '))
    c += 1
    if menor is None or num < menor:
        menor = num
    soma = ud + num
    ud = soma
    R = input('Deseja continuar? [S/N] ')
    if R.upper() == 'N':
        break
media = soma / (c - 1)
print(f'A soma entres os números foi {soma}')
print(f'O menor número digitado foi {menor}')
print(f'A média entres os valores digitados foi {media}')
