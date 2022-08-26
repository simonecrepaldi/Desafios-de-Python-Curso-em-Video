# Crie um programa que leia uma frase qualquer e dia se ela é um palíndromo, desconsiderando os espaços
# ex: apos a sopa | a sacada da casa | a torre da derrota | o lobo ama o bolo | Anotaram a data da maratona


# Transformando tudo em maiúsculas e excluindo todos os espaços vazios
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')

# Invertendo as letras
nfrase = ''.join(reversed(frase))
print('O inverso da frase digitada é: {}!'.format(nfrase))

# Verificando se a frase é um palíndromo
if frase == nfrase:
    print('Essa frase É UM PALÍNDROMO!')
else:
    print('Essa frase NÃO É UM PALÍNDROMO!')


# Outra forma de escrever o exercício usando o FOR':
frase2 = str(input('Digite uma frase: ')).strip().upper()

# Separando a frase em palavras e depois juntando todas sem espaço entre elas
palavras = frase2.split()
junto = ''.join(palavras)

inverso = ''
# Vai da última letra a primeira, voltado uma letra (por isso usa o -1)
for letra in range(len(junto) -1, -1, -1): 
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(frase2, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
