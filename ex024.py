km = int(input("Quantos km deseja percorrer? "))
if km <= 200:
    passagem = km * 0.50
    print(f"A passagem ficou por R${passagem}")
else:
   passagem = km * 0.45
   print(f"A passagem ficou por R${passagem}")
