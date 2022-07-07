print('---dados três números A, B e C escreva em ordem crescente---')
a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
if a <= b and b <= c:
    print(f'a ordem crescente é {a}, {b} e {c}.')
elif a <= c and c <= b:
    print(f'a ordem crescente é {a}, {c} e {b}.')
elif b <= a and a <= c:
    print(f'a ordem crescente é {b}, {a} e {c}.')
elif b <= c and c <= a:
    print(f'a ordem crescente é {b}, {c} e {a}.')
elif c <= a and a <= b:
    print(f' a ordem crescente é {c}, {a} e {b}.')
elif c <= b and b <= a:
    print(f'a ordem crescente é {c}, {b} e {a}.')


