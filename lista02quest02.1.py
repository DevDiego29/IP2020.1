print('---situação acadêmica---')
primNota = float(input('digite sua primeira nota: '))
segNota = float(input('digite sua segunda nota: '))
media = (primNota + segNota)/2
'''
if media >= 7:
    print(f'aluno está aprovado com média {media}')
elif media < 4:
    print(f'aluno está reprovado com média {media}')
else:
    print(f'aluno está apto a final com média {media}')
'''

if media >= 4 and media < 7:
    print(f' o aluno está apto a final com {media}')
elif media < 4:
    print(f'o aluno está reprovado com {media}')
else:
     print(f'o aluno está aprovado com {media}')
