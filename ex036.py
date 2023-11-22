hormes = int(input("Você fez quantas horas de atividadde fisica no mês? "))
pontos = 0
if hormes <= 10:
    pontos = 2 * hormes
else:
    if 10 < hormes <= 20:
        pontos = 5 * hormes
    else:
        pontos = 10 * hormes
troca = pontos * 0.05
print(pontos)
print(f"Você conseguiu {pontos} pontos esse mês.")
print(f"Você pode trocar por R${troca}")
