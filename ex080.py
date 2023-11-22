import random
chavez = 0
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
for i in range(0, 30):
    num[i] = random.randint(1, 15)

chave = int(input('Digite a chave: '))
print(num)
for i in range(0, 30):
    if num[i] == chave:
        print(f'A chave foi encontrada na posição {i}.')
        chavez += 1
print(f'A chave apareceu {chavez} vezes')
