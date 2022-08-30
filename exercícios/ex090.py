# Faça um programa que leia nome e média de uma aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Média >= 7 (aprovado), média < 7 (reprovado)

# Criando o dicionário "aluno"
aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# Verificando qual a situação do aluno de acordo com a média e adicionando o valor "situação" no dicionário "aluno"
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-'*40)

# Mostrando a chave (k) e os valores (v) dos items do dicionário
for k, v in aluno.items():
    print(f' - {k} é igual a {v}.')
print('-'*40)
