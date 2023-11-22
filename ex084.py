nome = ['', '', '', '', '', '', '', '', '', '']
idade = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 9):
    nome[i] = input(f'Digite o {i+1}° nome: ')
    idade[i] = int(input('Digite a idade dele(a): '))

for i in range(0, 9):
    if idade[i] < 18:
        print(f'{nome[i]} é menor de idade.')
