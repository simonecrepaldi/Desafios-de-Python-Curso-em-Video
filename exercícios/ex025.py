# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o seu nome completo: ')).strip()
nnome = nome.upper()
print('Você tem "Silva" no nome? {}'.format('SILVA' in nnome))

# Obs: Outra forma de escrever:
# print('Você tem "Silva" no nomme? {}'.format('SILVA' in nnome.upper()))
