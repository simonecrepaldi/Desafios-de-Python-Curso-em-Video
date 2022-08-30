# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# a) Quantas pessoas foram cadastradas 
# b) A média de idade 
# c) Uma lista com as mulheres 
# d) Uma lista de pessoas com idade acima da média

# Criando o dicionário "pessoa" e a lista "grupo"
pessoa = dict()
grupo = list()
soma = média = 0

while True:
# Limpando os dados da 'pessoa' depois de criar uma cópia dentro de 'grupo'
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
# Só aceita os valores "F" ou "M", se digitar outro informa o erro e continua perguntando o sexo da pessoa
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite F ou M!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
# Criando uma cópia da pessoa dentro da lista 'grupo'
    grupo.append(pessoa.copy())
# Enquanto a resposta não for "S" ou "N", mostra mensagem de erro e continua perguntando se quer adicionar mais alguém
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N!')
# Se digitar "N", interrompe o programa
    if resp == 'N':
        break
print('-'*30)

print(f'a) Ao todo temos {len(grupo)} pessoas cadastradas.')
# Calculando a média de idade
média = soma / len(grupo)
print(f'b) A média de idade é {média:.2f} anos.')
# Mostrando os nomes das mulheres (sexo == F)
print(f'c) As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
# Verificando se a idade é maior que a média de idade
print(f'd) Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('')
print('>>>>> ENCERRADO! <<<<<')
