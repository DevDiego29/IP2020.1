print('---Calculadora interativa---')
operação = input('''
Please type in the math operation you would like to complete:
+ for adição
- for subtração
* for multiplicação
/ for divisão
''')

number_1 = int(input('digite o primeiro número: '))
number_2 = int(input('digite o segundo número: '))

if operação == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operação == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operação == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operação == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('você não digitou um operador válido, execute o programa novamente')

calcular = input('''
deseja calcular novamente?
digite Y para sim e N para não.
''')

while calcular == 'Y':
    print('execute novamente')
    calcular =+1
if calcular == 'N':
    print('até mais')