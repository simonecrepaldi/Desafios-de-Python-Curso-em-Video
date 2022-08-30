# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m'}

print('* '*20)
print('{}Analisando os 10 termos da PA{}'.center(43).format(cores['roxo'], cores['limpa']))
print('* '*20)
a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
print('* '*20)
print('\033[1;33mOs 10 primeiros termos da PA são:\033[m')
termo = a
c = 1
while c <= 10:
    print('{}'.format(termo),  end=' → ')
    termo += r
    c += 1
print('{}FIM!{}'.format(cores['vermelho'], cores['limpa']))
