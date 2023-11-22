num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 1
for i in range(0, 9):
    num[i] = int(input(f'Digite o {c}° número: '))
    c += 1
for i in range(0, 9):
    if num[i] % 2 == 0:
        print(f'{num[i]} é par e está na posição {i}.')
