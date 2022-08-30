# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         'ciano':'\033[1;36m'}

print('* '*20)
print('{}Analisando os termos de uma PA{}'.center(43).format(cores['roxo'], cores['limpa']))
print('* '*20)

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

print('* '*20)
print('{}Os 10 primeiros termos da PA são:{}'.format(cores['ciano'], cores['limpa']))

termo = a
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo),  end=' → ')
        termo += r
        cont += 1
    print('{}PAUSA!{}'.format(cores['roxo'], cores['limpa']))
    mais = int(input('Quantos termos você deseja ver a mais: '))
print('{}A sessão foi finalizada com {} termos mostrados!{}'.format(cores['vermelho'], total, cores['limpa']))
