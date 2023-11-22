c = 1
ud = 0
idade = 0
soma = 0
div = 0
print('Se a idade dgitada for igual 999 ela será desconsiderada e o programa será finalizado.')
while idade != 999:
    idade = int(input(f'Digite a idade do {c}° aluno: '))
    c += 1
    if idade != 999:
        soma = ud + idade
        ud = soma
        div = c
media = soma / (div - 1)
print(f'Foram cadastradas as idades de {div-1} alunos.')
print(f'A média de idade da turma foi de {media} anos.')
