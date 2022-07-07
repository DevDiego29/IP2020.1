print('---Quais desses números são maiores que 10---')
lista = [] #lista dos números
num = 0 #variável de controle
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
num3 = int(input('digite o terceiro número: '))
num4 = int(input('digite o quarto número: '))
num5 = int(input('digite o quinto número: '))
if num1 > 10:
    print(f'então o {num1} é maior que 10')
    lista.append(num1)
if num2 > 10:
    print(f'então o {num2} é maior que 10')
    lista.append(num2)
if num3 > 10:
    print(f'então o {num3} é maior que 10')
    lista.append(num3)
if num4 > 10:
    print(f'então o {num4} é maior que 10')
    lista.append(num4)
if num5 > 10:
    print(f'então o {num5} é maior que 10')
    lista.append(num5)
print(f'a quantidade de números maiores que 10 são {lista}')