print('--- qual a categoria do nadador?')
idade = int(input('digite a sua idade: '))

if idade >= 5 and idade <=7:
    print('o atleta pertence a categoria INFANTIL A')
if idade >= 8 and idade <=10:
    print('o atleta pertence a categoria INFANTIL B')
if idade >= 11 and idade <=13:
    print('o atleta pertence a categoria JUVENIL A')
if idade >= 14 and idade <=17:
    print('o atleta pertence a categoria JUVENIL B')
elif idade > 18:
    print('o aleta pertence a categoria ADULTA')