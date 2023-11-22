n = 1
np = 0
ud = 0
print(n, end=' ')
for i in range(1, 10):
    fib = n + np
    np = n
    n = fib
    print(fib, end=' ')
