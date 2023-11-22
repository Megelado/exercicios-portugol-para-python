R = 'S'
maior = 0
maisVelha = ''
jovem = None
mulCad = 0
homCad = 0
aci30 = 0
men18 = 0
soma = 0
ud = 0
c = 1
while R.upper() == 'S':
     sexo = input('Qual o sexo: ')
     nome = input('Qual o nome: ')
     idade = int(input('Qual a idade: '))
     soma = ud + idade
     ud = soma
     c += 1
     if idade > maior:
         maior = idade
         maisVelha = nome
     if sexo.upper() == 'F':
         mulCad += 1
         if idade < 18:
             men18 += 1
         if jovem is None or idade < jovem:
             jovem = idade
             maisNova = nome
     if sexo.upper() == 'M':
         homCad += 1
         if idade > 30:
             aci30 += 1
             
     R = input('Deseja continuar? ')
print(f'A pessoa mais velha é {maisVelha}')
if mulCad >= 1:
     print(f'A mulher mais jovem foi {maisNova}')
media = soma / (c - 1)
print(f'A media de idade do grupo foi de {media} anos.')
if homCad == 1 and aci30 == 1:
     print('Há apenas um homen acima dos 30.')
else:
     if homCad > 1 and aci30 > 1:
         print(f'Há {aci30} homens acima dos 30.')
if mulCad == 1 and men18 == 1:
     print('Há apenas uma mulher abaixo dos 18.')
else:
     if mulCad > 1 and men18 > 1:
         print(f'Há {men18} mulheres abaixo dos 18.')

