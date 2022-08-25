# Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

# Importando a biblioteca random
from random import choice

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]

print('O aluno sorteado para apagar o quadro foi: {}'.format(choice(alunos)))
