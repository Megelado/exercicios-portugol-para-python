vi = int(input('Valor inicial: '))
vf = int(input('Valor final: '))
inc = int(input('Incremento: '))
if vf > vi:
    while vi <= vf:
        print(vi, end=' ')
        vi += inc
else:
    while vi >= vf:
        print(vi, end=' ')
        vi -= inc
print('Acabou!')

