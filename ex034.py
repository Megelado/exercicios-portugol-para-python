peso = float(input("Quanto ele pesa? "))
altura = float(input("Quanto ele mede em metros: "))
calculoImc = peso / (altura * altura)
if calculoImc < 18.5:
    IMC = "Abaixo do peso."
else:
    if 18.5 <= calculoImc < 25:
        IMC = "Peso Ideal"
    else:
        if 25 <= calculoImc < 30:
            IMC = "Sobrepeso"
        else:
            if 30 <= calculoImc < 40:
                IMC = "Obesidade"
            else:
                IMC = "Obesidade Mórbida"
print(calculoImc)
print(IMC)
