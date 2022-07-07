print('ler o nome completo de uma pessoa mostrando o primeiro e o último nome separadamente.')
nome_completo = str(input('Digite o seu nome completo: ')).strip() #strip é usado pra eliminar espaços antes e depois
nome = nome_completo.split() #split é usado para fatiar/dividir a string
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

#Fórmula para pegar sempre o último nome independente do tamanho:
#mostrar o nome na posição [len de nome - 1]
#len de nome = usado para saber quantas posição tem o nome completo