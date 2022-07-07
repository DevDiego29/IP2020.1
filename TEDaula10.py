print('Calcule a média aritmética dos elementos da matriz A = [[1,6,-9],[33,-6,88],[0,23,98]]')

matriz_A = [[1, 6, -9], [33, -6, 88],[0, 23, 98]]

media_aritmetica = 0

for i in range(3): #FOR para acessar as linhas
    for j in range(3): #FOR para acessar as colunas
        media_aritmetica = media_aritmetica + matriz_A[i][j]
media_aritmetica = media_aritmetica/9
print(media_aritmetica)