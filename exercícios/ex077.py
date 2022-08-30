# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Criando a tupla "frutas"
frutas = ('banana', 'abacaxi', 'maça', 'abacate', 'limao', 'laranja', 'pera', 'uva', 'melancia', 'amora', 'jabuticaba', 'mirtilo', 'framboesa', 'kiwi')

# upper() para colocar o nome da "fruta" em maiúsculas
for palavra in frutas:
    print(f'\nNa palavra \033[35m{palavra.upper()}\033[m temos as vogais: ', end='')

# lower() mostrar em minúscula as letras que estão em "aeiou"
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\033[36m{letra}\033[m', end=' ')
