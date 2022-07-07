print('---Calcule o perímetro e a área de um retângulo---')
altura = int(input('digite o valor do altura: '))
base = int(input('digite o valor da base: '))
perimetro = altura + base + altura + base #fórmula do perímetro do retângulo
area = altura * base #fórumla para se calcular a área de retângulo

print(f'o valor do perímetro é igual a {perimetro}')
print(f'o valor da área é igual a {area}')