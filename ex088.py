def ola(mensagem: str, numero: int):
    print('+-------=======------+')
    for i in range(1, numero+1):
        print(' ', msg)
    print('+-------=======------+')


msg = input('Gerador: ')
num = int(input('Digite quantas vezes deseja gerar: '))
ola(msg, num)
