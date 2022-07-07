print('Script para incrementar de 1 um a lista numérica de tamanho qualquer informada pelo usuário')
continua = 's' #variável de controle
lista = []
while continua == 's' or continua == 'S':
    n = int(input('digite um número qualquer: '))
    lista.append(n)
    continua = input('deseja continuar? (s/n): ')
print(lista)

for i in range(len(lista)):
    lista[i] = lista[i] + 1
print(lista)

'''print('Script para incrementar de 1 um a lista numérica de tamanho qualquer informada pelo usuário')
continua = 's' #variável de controle
lista = []
while continua == 's' or continua == 'S':
    n = int(input('digite um número qualquer: '))
    lista.append(n+1) 
    continua = input('deseja continuar? (s/n): ')
print(lista)
'''