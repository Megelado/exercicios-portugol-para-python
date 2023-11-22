def Contador(i, f, incr):
    print('Vai mostrar na tela ', end='')
    for i in range(i, f+1, incr):
        print(i, '>>', end=' ')


ini = int(input('Digite de onde a contagem irá começar: '))
fim = int(input('Digite onde termina a contagem: '))
incremento = int(input('Digite o incremento: '))
Contador(ini, fim, incremento)
print('FIM!')
