def Fibonacci(num):
    n = 1
    np = 0
    print('Vai gerar', end=' ')
    print(n, '>>', end=' ')
    for i in range(1, num):
        fib = n + np
        np = n
        n = fib
        print(fib, '>>', end=' ')


ter = int(input('Quantoos termos deseja ver? '))
Fibonacci(ter)
print('FIM!')
