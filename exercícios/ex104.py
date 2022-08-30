# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

# Definindo a função "leiaInt" que vai mostrar uma mensagem (msg)
def leiaInt(msg):
# Criando a variável 'ok'
    ok = False
    valor = 0
    while True:
# Aqui o programa vai ler o número 'n'
        n = str(input(msg))
# Se n for numérico, valor = n (valor digitado)
        if n.isnumeric():
            valor = int(n)
            ok = True
# Se o valor digitado não for numérico, mostrar a mensagem de erro e voltar para o 'while'
        else:
            print(f'\033[1;31mERRO! Digite um número inteiro válido!\033[m')
# Se o ok=True (n for numérico), interrompe o while
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'\033[1;32mVocê acabou de digitar o número {n}.\033[m')
