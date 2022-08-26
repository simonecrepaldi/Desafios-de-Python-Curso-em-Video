# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

somaidade = 0
maiorh = 0
nomevelho = 0
contm = 0

for pessoas in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoas))).title().strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoas)))
    sexo = str(input('F (feminino) ou M (masculino): '.format(pessoas))).upper()
    print('-'*50)
    somaidade += idade
    if sexo == 'M':
        if idade > maiorh:
            maiorh = idade
            nomevelho = nome
    else:
        if idade < 20:
            contm += 1
            
print('A média de idade do grupo é: {:.1f} anos'.format(somaidade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorh, nomevelho))
print('Quantidade de mulheres do grupo que tem menos de 20 anos: {}'.format(contm))
