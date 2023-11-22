nome = ['', '', '', '', '']
sal = [0, 1, 2, 3, 4]
sexo = ['', '', '', '', '']

for i in range(0, 5):
    nome[i] = input(f'Digite o {i+1}° nome: ')
    sal[i] = float(input('Qual o salário dele(a): '))
    sexo[i] = input('Qual o sexo: ')
for i in range(0, 5):
    if sexo[i].upper() == 'F' and sal[i] > 5000:
        print(f'{nome[i]} tem um salário de R${sal[i]}')
