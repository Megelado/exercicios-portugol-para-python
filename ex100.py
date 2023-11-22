def Media(n1, n2):
    med = (n1 + n2) / 2
    return med


def Situacao(media):
    situ = ''
    if media < 5:
        situ = 'reprovado!'
        return situ
    else:
        if 5 <= media < 7:
            situ = 'recuperação!'
            return situ
        else:
            situ = 'aprovado'
            return situ


nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
situacao = Situacao(Media(nota1, nota2))
if situacao == 'aeprovado':
    print('Voçe está', situacao)
else:
    if situacao == 'recuperação!':
        print('Voçe está de', situacao)
    else:
        print('Voçe está', situacao)
