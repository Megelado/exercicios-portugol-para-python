largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura * altura
areaT = round(area, 2)
print(f"A area total foi de {areaT}m²")
if areaT < 100:
    print("Terreno popular!")
else:
    if 100 <= areaT < 500:
        print("Terreno Master!")
    else:
        if areaT >= 500:
            print("Terreno vip!")
        else:
            print("Digite um valor válido!")
