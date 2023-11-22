nome = input("Qual o nome do(a) cliente? ")
sexo = input("Qual o sexo do(a) cliente? ")
valor = float(input("Qual o valor do produto comprado? "))
descontoHomem = valor * 5 / 100
descontoMulher = valor * 13 / 100
if sexo.upper() == "F":
    preco = valor - descontoMulher
    print(f"Com 13% de desconto ficou por apenas R${preco}")
else:
    preco = valor - descontoHomem
    print(f"Com 5% de desconto ficou por apenas R${preco}")
