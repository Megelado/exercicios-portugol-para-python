cigarros = int(input("Quantos cigarros você fuma por dia: "))
anos = int(input("Por quantos anos você fuma? "))
diasNoAno = anos * 365
estragoDia = cigarros * (- 10)
minutosEmAnos = 1440 * diasNoAno
diasPerdidos = estragoDia * diasNoAno
print(f"ele perdeu {round(diasPerdidos / 1440, 2)} dias ao longo dos anos.")
