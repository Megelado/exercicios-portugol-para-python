nota = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
ud = 0
maior = 0
for i in range(0, 10):
    nota[i] = int(input(f'Digite a {i+1}° nota: '))
    if nota[i] > maior:
        maior = nota[i]
    soma = ud + nota[i]
    ud = soma
media = soma / 10
print(f'A media da turma foi {media} pontos.')
acimed = 0
for i in range(0, 10):
    if nota[i] > media:
        acimed += 1
if acimed == 1:
    print('Há um aluno acima da média')
if acimed > 1:
    print(f'Há {acimed} alunos acima da média.')
print(f'A maior nota foi {maior}.')
for i in range(0, 10):
    if maior == nota[i]:
        print(f'A maior nota apareceu na posição {i}.')
