print('---situação acadêmica---')
primNota = float(input('digite a primeira nota: '))
segNota = float(input('digite a segunda nota: '))
media = (primNota + segNota)/2
if media >= 7:
    print(f'o aluno está aprovado com média {media}')
elif media < 4:
    print(f'o aluno está reprovado com média {media}')
else:
    print(f'o aluno está apto a final com média {media}')