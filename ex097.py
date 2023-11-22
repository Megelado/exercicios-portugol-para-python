def Maior(x, y, z):
    maior = 0
    igual = None
    if x > y and x > z:
        maior = x
    if y > x and y > z:
        maior = y
    if z > x and z > y:
        maior = z
    if x == y and x > z:
        return x
    else:
        if y == z and y > x:
            return y
        else:
            if x > y and x == z:
                return x
            else:
                igual = True
    if maior == x or maior == y or maior == z:
        return maior
    else:
        if igual:
            return igual
        else:
            return igual


n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
n3 = int(input('3° valor: '))
if Maior(n1, n2, n3) == True:
    print('Todos os valores digitados são iguais.')
else:
    print('O maior valor digitado foi ', Maior(n1, n2, n3))
