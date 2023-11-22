import random

p1 = input("Pedra, papel, tesoura? ")
numRan = random.randint(1, 3)
if numRan == 1:
    p2 = "Pedra"
else:
    if numRan == 2:
        p2 = "Papel"
    else:
        p2 = "Tesoura"
print(p2)
if p1.upper() == "PEDRA" and p2.upper() == "PEDRA":
    print("Deu empate!")
else:
    if p1.upper() == "PEDRA" and p2.upper() == "PAPEL":
        print("Player 2 venceu!")
    else:
        if p1.upper() == "PEDRA" and p2.upper() == "TESOURA":
            print("Player 1 venceu!")

if p1.upper() == "PAPEL" and p2.upper() == "PAPEL":
    print("Deu empate!")
else:
    if p1.upper() == "PAPEL" and p2.upper() == "TESOURA":
        print("Player 2 venceu!")
    else:
        if p1.upper() == "PAPEL" and p2.upper() == "PEDRA":
            print("Player 1 venceu!")

if p1.upper() == "TESOURA" and p2.upper() == "TESOURA":
    print("Deu empate!")

else:
    if p1.upper() == "TESOURA" and p2.upper() == "PEDRA":
        print("Player 2 venceu!")
    else:
        if p1.upper() == "TESOURA" and p2.upper() == "PAPEL":
            print("Player 1 venceu!")
