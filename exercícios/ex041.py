# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 25 anos: sênior
# Acima 25: master

# Importando a biblioteca
from datetime import date

ano = int(input('Informe o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade <=25:
    print('O atleta tem {} anos e está na categoria SÊNIOR!'.format(idade))
else:
    print('O atleta tme {} anos e está na categoria MASTER!'.format(idade))
    