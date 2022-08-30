# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Definindo a tupla
valores = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    número = int(input('Digite um número entre 0 e 20: '))

# Valor no intervalo de 0 a 20, encerra o programa e mostra o valor por extenso
    if 0 <= número <=20:
        break

# Se digitar um valor fora do intervalo de 0 a 20, mostra uma mensagem de erro
    print('\033[1;31m Valor incorreto! Tente novamente!\033[m')

print(f'O número digitado foi o \033[1;35m{valores[número]}\033[m!')


# Resolvendo com a biblioteca num2words
from num2words import num2words
numero = int( input('Digite um número: ') )
num_ptbr = num2words(numero, lang='pt-br')
print(f'O número foi:\033[1;33m {num_ptbr}\033[m')
