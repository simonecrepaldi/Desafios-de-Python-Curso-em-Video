# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Digite o seu nome completo: ')).strip().title()
nomes = nome.split()
print('Muito prazer em te conhecer, {}!'.format(nome))
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu último nome é: {}'.format(nomes[-1]))

# Obs: usando o title() deixamos a inicial de cada nome em maiúscula e as demais letras em minúscula
