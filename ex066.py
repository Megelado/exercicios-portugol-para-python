num = int(input('Digite o número que deseja ver a tabuada? '))
for c in range(1, 11):
    tabu = num * c
    print(f'{num} X {c} = {tabu}')
