c = 1
ud = 0
soma = 0
maigual21 = 0
while True:
    idade = int(input(f'Digite a idade da {c}a pessoa: '))
    if idade >= 21:
        maigual21 += 1
    c += 1
    soma = ud + idade
    ud = soma
    R = input('Quer continuar? [S/N] ')
    if R.upper() == 'N':
        break
media = soma / (c-1)
print(f'Foram digitadas {c-1} idades')
print(f'a media de idade digitadas foi de {media} anos.')
print(f'Há {maigual21} pessoas com idade igual ou maiores que 21.')
