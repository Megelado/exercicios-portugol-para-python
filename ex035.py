tipo = input("Digite o tipo de carro: [popular/luxo] ")
dias = int(input("Quantos dias: "))
km = float(input("Quantos km: "))
if tipo.upper() == "POPULAR":
    alupop = 90 * dias
    if km < 100:
        alukm = km * 0.2
        print(f"Você irá pagar no total R${alupop+alukm}")
    else:
        alukm = km * 0.1
        print(f"Você irá pagar no total R${alupop+alukm}")
if tipo.upper() == "LUXO":
    alulux = 150 * dias
    if km < 200:
        alukm = km * 0.3
        print(f"Você irá pagar no total R${alulux+alukm}")
    else:
        alukm = km * 0.25
        print(f"Você irá pagar no total R${alulux+alukm}")
