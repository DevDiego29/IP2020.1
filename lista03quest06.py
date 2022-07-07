print('--- Solução questão 06 lista 03 ---')
cont = 0 #contador para ler os 10 números
valor = 0
contImpares = 0 #variável para calcular a qnt de números impares
contPares = 0 #variável para calcular a qnt de números pares
somaPares = 0
somaImpares = 0
while cont < 10:
    valor = int(input(f'Digite um valor {cont+1}: '))
    if valor%2 == 0:
        contPares+=1
        somaPares = somaPares + valor
    else:
        contImpares+=1
        somaImpares = somaImpares + valor
    cont+=1
print('A quantidade de valores pares foi: ', contPares)
print('A quantidade de valores impares foi: ', contImpares)
print('a soma dos números pares é igual a: ', somaPares)
print('a média dos números impares é igual a: ',(somaImpares / contImpares))