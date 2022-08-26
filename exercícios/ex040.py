# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: reprovado
# Média entre 5.0 e 6.9: recuperação
# Média 7.0 ou superior: aprovado

cores = {'fim':'\033[m',
         'rep':'\033[1;31m',
         'apr':'\033[1;32m',
         'rec':'\033[1;33m'}
         
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
média = (n1+n2+n3)/3
print('')
if média < 5:
    print('Sua média foi {:.1f}, {}você está REPROVADO{}!'.format(média, cores['rep'], cores['fim']))
elif 5 <= média < 7:
    print('Sua média foi {:.1f}, {}você está de RECUPERAÇÃO{}!'.format(média, cores['rec'], cores['fim']))
elif 7 <= média:
    print('Sua média foi {:.1f}, {}você está APROVADO{}!'.format(média, cores['apr'], cores['fim']))
