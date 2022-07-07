print('Dado o nome completo de alguém informe: Nome em maiúsculas, em minúsculas, qnt total de letras do nome')
nome = str(input('digite o seu nome completo: '))
print('Fazendo uma análise do seu nome...')
print('seu nome em maiúsculo é {}'.format(nome.upper())) #deixar em maiusculo
print('seu nome em minúsculo é {}'.format(nome.lower())) #deixar em minusculo
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#len(nome) = ler a quantidade de caracteres #nome.count(' ') = não contar o espaço vazio entre os nomes
