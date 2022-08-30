# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# Definindo a função "voto"
def voto(ano):
# Importando a biblioteca para selecionar o ano atual do sistema
    from datetime import date
    atual = date.today().year
# Calculando a idade do usuário
    idade = atual - ano
    if idade < 16:
        return f'Você tem {idade} anos, \033[1;31mVOTO NEGADO\033[m!'
    elif idade < 18 or idade >= 70:
        return f'Você tem {idade} anos, \033[1;33mVOTO OPCIONAL\033[m!'
    else:
        return f'Você tem {idade} anos, \033[1;32mVOTO OBRIGATÓRIO!\033[m'


# Programa Principal
nascimento = int(input('Qual seu ano de nascimento? '))
print(voto(nascimento))
