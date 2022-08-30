# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('\033[31m-\033[m'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('\033[31m-\033[m'*40)

# Criando a tupla "produtos"
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

# Configurando para mostrar os dados de forma tabular
for pos in range(0, len(produtos)):

# Para mostrar o nome dos produtos, alinhados a esquerda, considerando 30 caracteres (preenchidos com "." após o nome)
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='.')
# Para mostrar os valores alinhados a direita, considerando 7 caracteres e com 2 casas decimais
    else:
        print(f'R${produtos[pos]:>7.2f}')
        
print('\033[31m-\033[m'*40)
