# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Criando uma lista em branco chamada "números"
números = list()

while True:
    n = int(input('Digite um valor: '))

# Se o número digitado (n) não estiver na lista (números), ele será adicionado pelo "números.append(n)"
    if n not in números:
        print('\033[1;32mValor adicionado com sucesso!\033[m')
        números.append(n)

# Caso ele já faça parte da lista, mostrar a mensagem de valor duplicado e que ele não será adicionado na lista
    else:
        print('\033[1;31mValor duplicado, não será adicionado!\033[m')

# Após o número ser adicionado na lista, perguntar se o usuário quer informar outro número, se a resposta for "N" o programa encerra
    resposta = str(input('Gostaria de adicionar mais um valor? [S/N] ')).upper()
    if resposta in 'N':
        break
print('-'*50)

# Mostrar os números em ordem crescente (sorted)
print(f'\033[1;35mOs números digitados foram: {sorted(números)}.\033[m')
