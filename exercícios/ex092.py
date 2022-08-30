# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (= 35 anos de contribuição).

# Importando a biblioteca
from datetime import datetime

# Criando o dicionário "pessoa"
pessoa = {}

pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))

# Calculando a idade a partir do ano de nascimento informada (ano) e o ano atual e adicionando no dicionário
pessoa['idade'] = datetime.now().year - ano

pessoa['ctps'] = int(input('Carteira de Trabalho (0 - não tem): '))

# Solicitando o número da CTPS (se for 0, não pede mais nada), ano de contratação e salário e adicionando no dicionário
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
# Calculando a idade com que a pessoa vai se aposentar
    pessoa['aposentadoria'] = ((35 + pessoa['contratação']) - datetime.now().year) + pessoa['idade']
print('-' * 40)

for k, v in pessoa.items():
    print(f'    - {k} tem valor o {v}.')
