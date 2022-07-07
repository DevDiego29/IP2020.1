print('---resolução questão 8 lista 2---')
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
soma = num1 + num2
if soma > 20:
    soma += 8
    print(f'o valor da soma é {soma}')
if soma <= 20:
    soma -= 5
    print(f'o valor da soma é {soma}')