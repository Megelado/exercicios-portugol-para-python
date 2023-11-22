c = 1
maior = 0
menor = None
while c <= 8:
    preco = float(input(f'Digite o {c}° preço: '))
    if preco > maior:
        maior = preco
    if menor is None or preco < menor:
        menor = preco
    c += 1
print(maior)
print(menor)
