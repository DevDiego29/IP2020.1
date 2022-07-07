print('digite 3 números e verifique se o primeiro é maior que soma dos outros')
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
num3 = int(input('digite o terceiro número: '))
soma = num2 + num3
if num1 > soma:
    print(f'então o {num1} é maior que soma de {num2} + {num3}')
else:
    print(f'então o {num1} não é maior que soma do {num2} + {num3}')