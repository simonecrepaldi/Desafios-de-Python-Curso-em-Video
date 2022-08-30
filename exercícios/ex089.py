# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Criando a lista "dados"
dados = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
# Criando a lista "dados" com as informações digitadas e a média calculada
    dados.append([nome, [nota1, nota2], média])

# Usuário deve informar se quer adicionar mais algum aluno, se a resposta for "N" o programa para
    resposta = str(input('Gostaria de cadastrar mais um aluno? [S/N] ')).upper()
    if resposta in 'N':
        break

# Mostrando a média de todos os alunos
print('BOLETIM DOS ALUNOS')
print('-'*25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# Usuário deve informar o número do aluno (se digitar 999 não mostra de mais nenhum)
while True:
    print('-'*35)
    opçao = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opçao == 999:
        print('FINALIZANDO...')
        break

# opçao é o número (posição) do aluno na lista, portanto só pode mostrar se o opçao for =< que o comprimento da lista "dados"
    if opçao <= len(dados) - 1: 
        print(f'Notas de {dados[opçao][0]} são {dados[opçao][1]}')

print('>>> Volte sempre! <<<')
