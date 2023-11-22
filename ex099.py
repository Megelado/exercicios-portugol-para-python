def Potencia(b, e):
    potencia = b ** e
    return potencia


base = int(input('Qual a base: '))
expoente = int(input('Qual o expoente: '))
print(Potencia(base, expoente))
