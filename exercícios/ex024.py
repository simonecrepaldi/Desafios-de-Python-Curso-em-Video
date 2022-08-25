# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

# Usando strip() removemos todos os espaços em branco do início e do fim da string e depois verificamos se temos no início da string (cidade[:5]) a palavra "Santo":
cidade = str(input('Digite a cidade onde você nasceu: ')).strip()
print('O nome da cidade começa com o nome "Santo"? {}'.format(cidade[:5].upper() == 'SANTO'))

# Obs: Outra forma de resolver, usando split() dividmos a string (cidade) em uma lista e em seguinda verificamos se na posição 0 temos a palavra "Santo":
# partescidade = cidade.split()
# print('O nome da cidade {} começa com o nome "Santo"?: {}'.format(cidade, 'Santo' in partescidade[0]))
