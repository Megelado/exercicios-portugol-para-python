def ola(mensagem: str, numero: int, esco: int):
    print(esco)
    for i in range(1, numero+1):
        print(' ', msg)
    print(esco)


msg = input('Gerador: ')
num = int(input('Digite quantas vezes deseja gerar: '))
print('Qual borda deseja? ')
print('Borda 1: +-------=======------+')
print('Borda 2: ~~~~~~~~:::::::~~~~~~~')
print('Borda 3: <<<<<<<<------->>>>>>>')
borda = int(input(''))
match borda:
    case 1:
         bordaesco = '+-------=======------+'
    case 2:
         bordaesco = '~~~~~~~~:::::::~~~~~~~'
    case 3:
         bordaesco = '<<<<<<<<------->>>>>>>'
ola(msg, num, bordaesco)
