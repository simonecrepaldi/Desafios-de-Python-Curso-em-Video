# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('Na frase digitada a letra "A" aparecer {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}.'.format(frase.find('A')))
print('A letra "A" aparece a última vez na posição {}.'.format(frase.rfind('A')))

# Obs: rfind: começa a contar pela direita
