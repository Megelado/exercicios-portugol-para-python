nome = ['', '', '', '', '', '', '']
c = 1
for i in range(7-1, -1, -1):
    nome[i] = input(f'Digite o {c}° nome: ')
    c += 1
print(nome)
