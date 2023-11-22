segmento1 = int(input("Digite o valor do primeiro segmento: "))
segmento2 = int(input("Digite o valor do segundo segmento: "))
segmento3 = int(input("Digite o valor do terceiro segmento: "))
if (segmento1 < segmento2+segmento3) and (segmento2 < segmento1+segmento3) and (segmento3 < segmento1+segmento2):
    print("É possivel formar um triângulo com as medidas passadas.")
else:
    print("Não é possivel formar um triângulo com as medidas passadas.")
