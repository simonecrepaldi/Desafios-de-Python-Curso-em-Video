# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Criando a lista "numeros" e deixando ela vazia
numeros = []
maior = menor = 0

# Fazendo o usuário informar 5 números e usando o "numeros.append" para colocar os valores na lista
for cont in range(0, 5):
    numeros.append(int(input(f'Digite o valor da posição {cont}: ')))

# Para o primeiro valor digitado (cont == 0), o valor da posição 0 (numeros[0]) será o menor e o maior valor da lista
    if cont == 0:
        maior = menor = numeros[cont]

# A partir do segundo valor, temos que verificar se ele é maior ou menor que os valores digitados
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]

print('-'*50)
print(f'\033[1;35mOs valores digitados foram: {numeros}\033[m')
print(f'O maior valor digitado foi o {maior} nas posições: ', end='')

# Verificando a posição (i = índice) do maior número (v = valor)
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
# Verificando a posição (i = índice) do menor número (v = valor)
print(f'O menor valor digitado foi o {menor} nas posições): ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')


# Obs: Fazendo da forma apresentada a seguir, só funciona se os 5 números forem diferentes. Caso digite dois ou mais números iguais, ele só vai mostrar a primeira posição do número
números = list()
for c in range(0, 5):
    números.append(int(input('Digite um número: ')))
print('-' * 45)
print(f'Os números digitados foram: {números}')
valores = sorted(números)
print(f'> O maior valor digitado é o \033[1;31m{valores[4]}\033[m na posição \033[1;31m{números.index(valores[4])}\033[m.')
print(f'> O menor valor digitado é \033[1;31m{valores[0]}\033[m na posição \033[1;31m{números.index(valores[0])}\033[m.')
