R = 'S'
usdmul = 0
usdhom = 0
salhom = 0
salmul = 0
somamul = 0
somahom = 0
while R.upper() == 'S':
    sexo = input('Qual o sexo? ')
    sal = float(input('Qual o salário: '))
    R = input('Deseja continuar? [sim/nao] ')
    if sexo.upper() == 'F':
        salmul = sal
        somamul = usdmul + salmul
        usdmul = somamul
    if sexo.upper() == 'M':
        salhom = sal
        somahom = usdhom + salhom
        usdhom = somahom
if somahom > 0:
    print(f'O salário pago aos homens foi de R${somahom}')
else:
    print('Não foi pago nenhum salário a nenhum homen.')
if somamul > 0:
    print(f'O salário pago as mulheres foi de R${somamul}')
else:
    print('Não foi pago nenhum salário a nenhuma mulher.')
