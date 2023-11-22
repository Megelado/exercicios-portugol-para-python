c = 1
hom = 0
mul = 0
idahom = 0
soma = 0
somageral = 0
ud = 0
udgeral = 0
acivinte = 0
while c <= 5:
    idade = int(input(f'Digite a idade de {c}° pessoa: '))
    sexo = input('Digito o sexo dela: ')
    somageral = udgeral + idade
    udgeral = somageral
    if sexo.upper() == 'M':
        hom += 1
        idahom = idade
        soma = idahom + ud
        ud = soma
    if sexo.upper() == 'F':
        mul += 1
        idademul = idade
        if idade > 20:
            acivinte += 1
    c += 1
medgeral = somageral / 5
if hom != 0:
    med = soma / hom
    print(f'A média de idade dos homens foi {round(med, 2)} anos.')
    print(f'Foram cadastrados {hom} homens')
else:
    print('Não foi cadastrado nenhum homen')
if mul == 1:
    print('Foi cadatrada apenas uma mulher.')
else:
    if mul > 1:
        print(f'Foram cadastradas {mul} mulheres')
    else:
        print('Não foi cadastrada nenhuma mulher.')
print(f'A média de idade do grupo foi de {medgeral} anos.')
if mul == 1 and idade > 20:
    print('Há apenas uma mulher acima dos vinte.')
else:
    if mul > 1 and idademul > 20:
        print(f'Há {acivinte} mulheres acima dos vinte.')
