mulCad = 0
pesado = 0
ud = 0
soma = 0
maior = 0
for c in range(1, 9):
    sexo = input('Qual o sexo? ')
    peso = float(input(f'Digite o peso: '))
    if sexo.upper() == 'F':
        mulCad += 1
        pesomul = peso
        soma = ud + pesomul
        ud = soma
    if sexo.upper() == 'M' and peso > 100:
        pesado += 1
    if sexo.upper() == 'M':
        if peso > maior:
            maior = peso
media = soma / mulCad
print(f'Foram cadastradas {mulCad} mulheres.')
print(f'Há {pesado} homens com mais de 100 kilos.')
print(f'O peso médio das mulheres foi de {media} kilos')
print(f'O homem mais pesado tem {maior} kilos')
