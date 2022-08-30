# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
pares = []
ímpares = []

# Solicitando os 7 números
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))

# Verificando se o número digitado é par e, se for, adicionar na lista "pares"
    if num % 2 == 0:
        pares.append(num)
# Se o número não for par, adicionar na lista "ímpares"
    else:
        ímpares.append(num)

# Adiciona a lista "pares" e a lista "ímpares" na "lista" e coloca todos os números em ordem crescente (lista.sort)
lista.append(pares[:])
lista.append(ímpares[:])
lista.sort()

print('-'*50)
print(f'Os valores digitados foram: {lista}')
print(f'Valores ímpares: {ímpares}')
print(f'Valores pares: {pares}')


# Obs: Outra forma de resolver o problema
números = [[], []]
valor = 0

for c in range (1, 8):
    valor = int(input(f'Digite o {c}º valor: '))

# Se o número for par, adicionar ele na lista "números" na posição 0
    if valor % 2 == 0:
        números[0].append(valor)
# Se o número for ímpar, adicionar ele na lista "números" na posição 1
    else:
        números[1].append(valor)
# Organizando as duas listas de "números" em ordem crescente
números[0].sort()
números[1].sort()
print(f'Valores pares: {números[0]}')
print(f'Valores ímpares: {números[1]}')
