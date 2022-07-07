print('Lista 04 questão 02')
def calcular_pagamento(qnt_horas, valor_hora): #Criando a função que recebe dois parâmentros
    horas = float(qnt_horas) #valores convertidos para o tipo float, pois serão recebido como uma str
    taxa = float(valor_hora)
    if horas <= 40: #se a qnt de horas trabalhadas for < 40h
        salario = horas * taxa #multiplicamos a quantidade de horas * o valor de cada hora
    else: #Caso seja > 40h trabalhadas
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    return salario

str_horas = input('digite as horas: ')
str_taxa = input('digite a taxa: ')
total_salario = calcular_pagamento(str_horas, str_taxa)
print('o valor de seus rendimentos é R$', total_salario)