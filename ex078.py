c = 1
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i in range(0, 15):
    num[i] = int(input(f'Digite o {c}° número: '))
    c += 1
print(num)
for i in range(0, 15):
    if num[i] % 10 == 0:
        print(f'Na posição {i} o número {num[i]} é divisivel por 10.')
