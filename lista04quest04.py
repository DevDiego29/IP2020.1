import lista04quest04a #importou uma função a partir de outro arquivo

def main():
    print('-- ESTE PROGRAMA CALCULA MEDIAS ---')
    tipoMedia = input('Digite a media desejada: '
                            'a para aritmedia: '
                            'p para ponderada'
                            'h para harmônica')
    print('Agora, vamos ler o valores...')
    a = float(input('Digite o valor: '))
    b = float(input('Digite o valor: '))
    c = float(input('Digite o valor: '))
    print(lista04quest04a.calcMedia(a, b, c, tipoMedia))

main() #esse main utilizo para chamar toda a função