nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5:
   print("Reprovado!")
else:
   if 5 <= media < 7:
      print("Em recuperação!")
   else:
      if media >= 7:
         print("Aprovado!")
