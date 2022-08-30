# Definindo a função "leiaInt"
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

# Definindo a função "linha", se não definir o tamanho, assume o valor 42
def linha(tam = 42):
    return '-' * tam

# Definindo a função "cabeçalho"
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# Definindo a função "menu"
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc
