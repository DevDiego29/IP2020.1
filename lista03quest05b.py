#Usando o WHILE

print('=== GERADOR DE TABUADA === ')
print()
n1 = int(input('Deseja ver a tabuada de: '))
cont = 1
while cont < 10:
    tab = n1 * cont
    print()
    print(n1, 'x', cont, '= ', tab)
    cont += 1