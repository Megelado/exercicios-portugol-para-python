n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print(f"{n1} é o maior.")
else:
    if(n2 > n1):
        print(f"{n2} é o maior.")
    else:
        print("Os dois valores digitados são iguais.")
