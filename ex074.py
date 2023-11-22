num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 10):
    if num[i] % 2 == 0:
        num[i] = 5
    else:
        num[i] = 3

print(num)
