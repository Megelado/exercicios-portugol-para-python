import random

vitoria = False
c = 1
numRan = random.randint(1, 10)
print(numRan)
while c <= 4:
    tent = int(input("Tente adivinhar o número sorteado: "))
    if tent == numRan:
        print(f"Parabéns o número {tent} foi o sorteado, você acertou!")
        c = 4
        vitoria = True
    c += 1
if vitoria == False:
    print(f"Infelizmente você errou, o número digitado foi {numRan}")
