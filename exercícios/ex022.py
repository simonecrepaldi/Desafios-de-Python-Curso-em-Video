# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

# Colocar strip() para eliminar todos os espaços do início e do final
nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome.replace(' ', ''))))
partesnome = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras.'.format(partesnome[0], len(partesnome[0])))

# Obs1: Outra forma de fazer a contagem das letras é:
# print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

# Obs2: Outra forma de fazer a contagem de letras do primeiro nome é encontrar a posição do primeiro espaço:
#print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
