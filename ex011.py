print("Equacao de 2 grau completa:")
print("AX² + BX + C = 0")
a = int(input("Digite o valor equivalente a A: "))
b = int(input("Digite o valor equivalente a B: "))
c = int(input("Digite o valor equivalente a C: "))
print("")
delta = b * b - 4 * a * c
b2 = b * b
a2 = -4 * a
ope1 = a2 * c
delpos = b2 + ope1
print(f"{b} x {b} -4 x {a} x {c}")
print(f"{b2} -4 x {a} x {c}")
if a2 >= 0 and ope1 >= 0:
    print(b2, " + ", a2, " x ", c)
    print(b2, " + ", ope1)
else:
    print(b2, a2, " x ", c)
    if ope1 >= 0:
        print(b2, " + ", ope1)
    else:
        print(b2, ope1)
    print(delpos)
print("")
print("O valor de delta foi ", delta)
