# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# a) Quantas pessoas tem mais de 18 anos;
# b) Quantos homens foram cadastrados;
# c) Quantas mulheres tem menos de 20 anos.

cores = {'amarelo':'\033[1;33m',
         'fim':'\033[m'}

cont = maiores = homem = mulher = 0

while True:
    print('-' * 30)
    print('{}CADASTRO DE PESSOAS{}'.center(33).format(cores['amarelo'], cores['fim']))
    print('-'*30)
    idade = int(input('Idade: '))

# Vai repetir a pergunta até que o usuário responda "F" ou "M"
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]

# Vai repetir a pergunta até que o usuário responda "S" ou "N", se responder "N" o programa encerra
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).upper().strip()[0]
    cont += 1

    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1

# Se a idade >= 18 conta +1 em "maiores"
    if idade >= 18:
        maiores += 1
    if mais == 'N':
        break

print('-' * 30)
print('{}>>> PROGRAMA ENCERRADO! <<<{}'.center(34).format(cores['amarelo'], cores['fim']))
print(f'- Entre as {cont} pessoas cadastradas, {maiores} tem mais de 18 anos.')
print(f'- Total de homens cadastrados: {homem}.')
print(f'- Total de mulheres com menos de 20 anos: {mulher}.')
