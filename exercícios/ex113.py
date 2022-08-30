# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Defininco a função "leiaInt"
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n

# Definindo a função "leiaFloat"
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


# Programa Principal
a = leiaInt('Digite um número inteiro: ')
b = leiaFloat('Digite um valor real: ')
print(f'\033[1;35mVocê digitou o número inteiro {a} e o real {b}.\033[m')
