R = 'S'
maior = 0
homCad = 0
jovem = None
ud = 0
soma = 0
mulCad = 0
while R.upper() == 'S':
     sexo = input('Qual o sexo? ')
     idade = int(input('Qual a sua idade? '))
     R = input('Deseja continuar? ')
     if idade > maior:
         maior = idade
     if sexo.upper() == 'M':
         homCad += 1
         idadehom = idade
         soma = ud + idadehom
         ud = soma
     if sexo.upper() == 'F':
         mulCad += 1
         if jovem is None or idade < jovem:
             jovem = idade
print(f'A maior idade lida foi {maior}')
if homCad == 1:
     media = soma / homCad
     print(f'Foi cadastrado apenas {homCad} homem.')
else:
     if homCad > 1:
         media = soma / homCad
         print(f'Foram cadastrados {homCad} homens.')
         print(f'A média de idade dos homens cadastrados foi de {round(media, 2)} anos')
if mulCad != 0:
     print(f'A idade da mulher mais jovem foi de {jovem} anos')


