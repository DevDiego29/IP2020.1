print('---resolução da questão 6 lista 3 ---')
lista = [] #aqui serão serão armazenados os números
cont = 0
valor = 0
contImpares = 0 #variável para calcular a qnt de números ímpares
contPares = 0 #variável para calcular a qnt de números pares
somaPares = 0 #variável para calcular a soma dos números pares
somaImpares = 0 #variável para calcular a soma dos números ímpares
mediaImpares = 0 #variável para calcular a média de números ímpares
while cont < 10:
    valor = int(input(f'Digite um valor {cont+1}: '))
    lista.append(valor)
    if valor%2 == 0:
        contPares+=1
    else:
        contImpares+=1
    cont+=1
print('A quantidade de valores pares foi: ', contPares)
print('A quantidade de valores impares foi: ', contImpares)
for item in lista:
    if (item % 2 == 0):
        somaPares += item
    else:
        somaImpares += item
mediaImpares = somaImpares/contImpares
print(f'a soma dos números pares é {somaPares} e a média dos números ímpares é {mediaImpares}')
