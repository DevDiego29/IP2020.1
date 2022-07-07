#receba um número inteiro, calcule e escreva a tabuada 1 a 10 desse número

#Usando o FOR
#Opção 1 de resposta:

tabuada = int(input("Tabuada do numero: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))

#Opção 2 de resposta:

'''numero= int(input("Qual tabuada voce quer saber? Digite um numero de 1 a 10.\n"))
print(" Tabuada do ",numero,":\n")
for i in range(1,11):
    print(numero," X ",i," = ",numero*i, "\n")'''