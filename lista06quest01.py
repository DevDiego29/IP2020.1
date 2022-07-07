print('ler o nome completo de uma pessoa e verificar se existe o sobrenome Silva')

#Versão 1:
nome = str(input('Digite seu nome: ')).title() #title() = transforma a primeira palavra de cada letra em maiúsculo;
if 'Silva' in nome:
    print('Possui Silva')
else:
    print('Não possui Silva')

#Versão 2:
nomeC = str(input('Informe seu nome completo: '))
sobreN = 'Silva' in nomeC #existe 'Silva' dentro do nomeC
if sobreN == False:
    print('Em seu nome não existe Silva.')
else:
    print('Seu nome contém Silva.')

#Versão 3:
'''nome = 'Diego Rodrigues Silva'
if 'Silva' in nome:
    print('encontrei!')
else:
    print('Não encontrei!')'''

#Versão 4:
'''str1 = input('Digite o seu nome e sobrenome: ')
str2 = 'Silva'
if str2 in str1 or 'Silva' in str1: 
    print('o nome digitado contém Silva')
else:
    print('o nome digitado não contém Silva')'''

#Versão 5:
'''nome = input('Digite o seu nome completo: ')
if 'Silva' in nome:
    print('Sobrenome Silva encontrado')
    print(f'nome completo: {nome}')
else:
    print('Sobrenome Silva não encontrado')'''

#Versão 6:
nome = input('Digite seu nome completo: ')
nome_split = nome.split()

if 'Silva' in nome_split:
    print('Existe Silva')
else:
    print('Não existe Silva')


