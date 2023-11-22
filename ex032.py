import random

numRan = random.randint(1, 5)
tent = int(input("Tente adivinhar o número sorteado: "))
if tent == numRan:
    print(f"Parabéns o número {tent} foi o sorteado, você acertou!")
else:
    print(f"Infelizmente você errou, o número digitado foi {numRan}")
