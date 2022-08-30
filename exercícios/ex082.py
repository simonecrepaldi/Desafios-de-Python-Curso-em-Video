# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente Ao final, mostre o conteúdo das três listas geradas.

# Criando as listas: lista, pares e ímpares
lista = []
pares = []
ímpares = []

# Solicita que o usuário informe um número e adiciona ele na lista
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Quer continuar? [S/N] ')).upper()

# Se o usuário responder "N" encerra o programa
    if resp in 'N':
        break

# Colocando os elementos da "lista" em ordem crescente
lista.sort()

# Verificando se o número informado é par e, se for, adicionar na lista "par"
for n in lista:
    if n % 2 == 0:
        pares.append(n)
# Se o número não for par, adicionar na lista "ímpar"
    else:
        ímpares.append(n)

print('.'*50)
print(f'\033[1;35mOs valores digitados foram: {lista}\033[m')
print(f'\033[1;33mNúmeros pares da lista: {pares}\033[m')
print(f'\033[1;34mNúmeros ímpares da lista: {ímpares}\033[m')
