print('-- resolução questão 6 da lista 3---')
lista = [] #lista onde serão armazenados os números
pares = 0 #variável para calcular a qnt de números pares
impares = 0 #variável para calcular a qnt de números ímpares
soma_Pares = 0 #variável para calcular a soma dos números pares
soma_Impares = 0 #variável para calcular a soma dos números ímpares
media_impares = 0 #variáosvel para calcular a média de números ímpares
maiores = 0 #variável para calcular a qnt de números maior que a média dos ímpares
count = 1 #contador para ler os 10 números
# lendos os 10 números e colocando na lista
while count <=10:
    num = int(input(f'digite o {count}º número: '))
    lista.append(num)
    count += 1
#imprime lista
#print('lista:', lista)
#calculando a qnt de números pares/impares
for item in lista:
    if (item % 2 == 0):
        pares += 1
    else:
        impares += 1
#print da quantidade
print(f'foram lidos {pares} números pares e {impares} números ímpares.')
#Calculando a soma dos números pares e soma dos números ímpares (para fazer a média dos ímpares)
for item in lista:
    if (item % 2 == 0):
        soma_Pares += item
    else:
        soma_Impares += item
#calculando a média dos ímpares
media_impares = soma_Impares/impares
#print do resultado
print(f'a soma dos números pares é {soma_Pares} e a média dos números ímpares é {media_impares}')
#calculando a qnt de números maiores que a média dos números ímpares
for item in lista:
    if item > media_impares:
        maiores += 1
#print do resultado
print(f'{maiores} números são maiores que a média dos números ímpares lidos.')