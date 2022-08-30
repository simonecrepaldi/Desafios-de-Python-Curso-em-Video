# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a) Quantas pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) Uma listagem com as pessoas mais leves.

# Criando as listas "grupo" e "dado"
grupo = list()
dado = list()
maior = menor = 0

# Solicitando o nome e o peso da pessoa e adicionando na lista "dado"
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

# Para a primeira pessoa adicionada na lista, o peso será o menor e o maior
    if len(grupo) == 0:
        maior = menor = dado[1]
# Para as demais pessoas adicionadas, verificar se o peso é maior ou menor que o peso da pessoa anterior  
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]

# Adicionar os dados da pessoa na lista "grupo" e limpar a lista "dado" (dado.clear)
    grupo.append(dado[:])
    dado.clear()

# Perguntar se o usuário quer adicionar mais uma pessoa e, se a resposta for "N", encerrar o programa
    resp = str(input('Deseja cadastrar mais alguém? [S/N] ')).upper()
    if resp in 'N':
        break

print('.'*55)
print(f'\033[1;35ma) Total de pessoas cadastradas: {len(grupo)}\033[m')

print(f'b) Maior peso cadastrado é {maior:.2f}kg. Pessoas: ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()

print(f'c) Menor peso cadastrado é {menor:.2f}kg. Pessoas: ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
