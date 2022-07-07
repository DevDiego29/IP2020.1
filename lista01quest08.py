print('---qual o valor da prestação em atraso?---')
valor = int(input('digite o valor da prestação: '))
taxa = int(input('digite o valor da taxa de juros: '))
tempoAtraso = int(input('digite o tempo de atraso: '))
prestação = valor + (valor * (taxa/100) * tempoAtraso)  #fórmula
print(f'o valor da prestação em atraso será de {prestação}')