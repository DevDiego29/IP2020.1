print('Quantos elementos da matriz são menores que zero:A = [[1,6,-9],[33,-6,88],[0,23,98]]')

contNegativos = 0

Matriz_A = [[1, 6, -9],
            [33, -6, 88],
            [0, 23, 98]]

for l in range(3):
    for c in range(3):
        if Matriz_A[l][c] < 0:
            contNegativos+=1

print('a quantidade numeros negativos é ', contNegativos)