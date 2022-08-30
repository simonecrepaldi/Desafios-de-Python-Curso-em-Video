# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

# Criando a tupla "números" com os 4 valores que o usuário vai informar
números = (int(input('Digite o primeiro valor: ')),
          int(input('Digite o segundo valor: ')),
          int(input('Digite o terceiro valor: ')),
          int(input('Digite o quarto valor: ')))

print(f'Os números digitados foram: {números}')
print('-'*50)

# count(9) conta a quantidade de vezes que o "9" foi digitado 
print(f'a) O número 9 foi digitado {números.count(9)} vezes.')

# Verificando se o "3" faz parte da tupla, index mostra a posição do "3" (como a posição começa em 0, o "+1" vai mostrar a partir do 1)
if 3 in números:
    print(f'b) O número 3 apareceu a primeira vez na {números.index(3)+1}ª posição.')
# Se não tiver "3", mostra a mensagem abaixo
else:
    print('b) O número 3 não foi digitado em nenhuma posição.')

# Verificando quais valores são pares
print('c) Os valores pares digitados foram: ', end='')
for n in números:
    if n % 2 == 0:
        print(n, end=', ')
