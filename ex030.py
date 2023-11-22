segmento1 = int(input("Digite o valor do primeiro segmento: "))
segmento2 = int(input("Digite o valor do segundo segmento: "))
segmento3 = int(input("Digite o valor do terceiro segmento: "))
if (segmento1 < segmento2+segmento3) and (segmento2 < segmento1+segmento3) and (segmento3 < segmento1+segmento2):
    print("É possivel formar um triângulo com as medidas passadas.")
    if segmento1 == segmento2 and segmento2 == segmento3:
        print("Pode formar um triângulo equilátero!")
    else:
        if ((segmento1 == segmento2 and segmento1 != segmento3) or (segmento2 == segmento3 and segmento2 != segmento1)
                or (segmento3 == segmento1 and segmento3 != segmento2)):
            print("É possivel fazer um triângulo isósceles!")
        else:
            if segmento1 != segmento2 and segmento1 != segmento3 and segmento2 != segmento3:
                print("É possivel fazer um triângulo escaleno!")
else:
    print("Não é possivel formar um triângulo com as medidas passadas.")
