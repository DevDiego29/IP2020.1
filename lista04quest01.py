#Implementação das funções! parâmetros formais!
def calAreaTriangulo(base, altura): #Criando uma função e (colocar os parâmetros)
    return (base * altura)/2 #retornar um valor resultante

def calAreaCirculo(raio):
    return 3.14 * raio*raio  #pow(raio, 2) #raio**2 (potenciação, como se fosse raio elevado ao quadrado) #pi = 3,14

def calAreaQuadrado(lado):
    return lado * lado    #lado**2

#Chamada das funções! parâmetros reais!

#letra a:
print('area do triângulo é', calAreaTriangulo(3,10))

#letra b:
print('area do circulo é', calAreaCirculo(5))

#letra c:
print('area do quadrado é', calAreaQuadrado(4))

#letra d:
area = calAreaQuadrado(5.7) + 2 * calAreaCirculo(3.5) + calAreaTriangulo(4, 3)
print('a area do terreno é', area)