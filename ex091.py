def Maior(x, y):
    z = 0
    maior = 0
    if x > y:
        maior = x
    if y > x:
        maior = y
    if x == y:
        maior = z
    if maior == x or maior == y:
        print(f'O maior valor digitado foi {maior}')
    else:
        if maior == z:
            print('Os dois valores digitados foram iguais.')
        else:
            print('Um ou os dois valores digitados não foram válidos.')


n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
Maior(n1, n2)
