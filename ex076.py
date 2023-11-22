import random
num = [1, 2, 3, 4, 5, 6, 7]
for i in range(1, 7):
    ale = random.randint(1, 20)
    num[i] = ale
print(num)
