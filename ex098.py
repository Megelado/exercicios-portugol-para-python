def SuperSomador(ini, fim):
    soma = 0
    ud = 0
    for i in range(ini, fim + 1):
        iatu = i
        soma = ud + iatu
        ud = soma
    return soma


com = int(input('digite o número que iniciará a contagem: '))
ter = int(input('Digite o número que irá encerrar a contagem: '))
print(f'A soma dos números entre {com} e {ter} foi ', SuperSomador(com, ter))
