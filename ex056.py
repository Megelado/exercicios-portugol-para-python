num = 0
ud = 0
soma = 0
while num != 1111:
    num = int(input('Digite um número: '))
    print('Se desejar parar digite 1111')
    if num != 1111:
        soma = ud + num
        ud = soma
print(soma)
