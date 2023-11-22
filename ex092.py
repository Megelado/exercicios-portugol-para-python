def ParOuImpar(n):
    if n % 2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')


num = int(input('Digite um número inteiro: '))
ParOuImpar(num)
