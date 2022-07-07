print('função que recebe um vetor de 10 elementos, por parâmetro, e retorna a soma de todos os seus elementos')

'''soma = sum([10, 20, 30, 5, 35, 70, 12, 78, 90, 100]) #usando a função sum
print(soma)'''

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

print(somalista([10, 20, 30, 5, 35, 70, 12, 78, 90, 100]))


