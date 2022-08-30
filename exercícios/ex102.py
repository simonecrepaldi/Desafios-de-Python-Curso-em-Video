# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# Definindo a função "fatorial"
def fatorial(n, show=False):
# Docstring
    """
    Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial do número n.
    """
    f = 1
# Cálculo do fatorial
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
# Vai mostrar o 'x' logo depois dos números
            if c > 1:
                print(' x ', end='')
# Quando chegar no 1 vai mostrar o '='
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
# Se deixar "True" vai mostrar o cálculo
print(fatorial(5, show=True))
