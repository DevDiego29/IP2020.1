"""
@param primValor primeiro valor a entrar no calculo da media
@param segValor ''
@param terValor ' '
@param tipoMedia ''
@return: retorna o calculo da média especificada por tipoMedia.
Para valores inválidos retorna -1
"""

def calcMedia(primValor, segValor, terValor, tipoMedia):
    if tipoMedia == 'a' or tipoMedia == 'A': #se o tipoMedia for 'a' ou 'A' terei que calcular a média aritmética
        return (primValor+segValor+terValor)/3
    elif tipoMedia == 'p': #senão se for 'p' = média ponderada
        return (primValor*5+segValor*3+terValor*2)/10
    elif tipoMedia == 'h': # senão se for 'h' = média harmônica
        return (3/((1/primValor)+(1/segValor)+(1/terValor))) #quantidade de valores, dividido pelo inverso de cada um
    else:
        return -1 #caso seja inválido retorna -1

print(calcMedia(10,20,30,'h'))