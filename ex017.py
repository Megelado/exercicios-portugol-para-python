vel = float(input("Qual a velocidade do carro? "))
if vel > 80:
    multa = (vel - 80) * 5
    print(f"Você foi multado!A multa foi de R${round(multa, 2)}")
