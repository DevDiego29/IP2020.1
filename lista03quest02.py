print('--- Versão 02 da Média Aluno ---')
primNota = float(input('Digite a primeira nota: '))
while primNota < 0 or primNota > 10:
    primNota = float(input("Nota Inválida!! Digite novamente: "))

segNota = float(input('Digite a segunda nota: '))
while segNota < 0 or segNota > 10:
    segNota = float(input("Nota Inválida!! Digite novamente: "))

media = (primNota + segNota)/2
if media >= 7:
    print('APROVADO')
elif media < 4:
    print('REPROVADO')
else:
    print('APTO A FINAL')