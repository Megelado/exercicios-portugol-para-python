n = 1
np = 0
ud = 0
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(0, 16):
    fib = n + np
    np = n
    n = fib
    num[i] = fib
print(num)
