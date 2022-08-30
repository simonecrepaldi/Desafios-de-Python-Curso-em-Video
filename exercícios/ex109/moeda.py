# Definindo a função "aumentar"
def aumentar(preço=0, taxa=0, formato=False):
    """
    Cálcula o aumento de um preço em função de uma taxa (%).
    :param preço: preço informada para o cálculo.
    :param taxa: taxa (%) informada que será aumentada no preço.
    :param formato: se False - resultado não formatado, se True - resultado formatado.
    :return: retorna o resultado do cálculo.
    """
    res = preço + ((preço * taxa) / 100)
    return res if formato is False else moeda(res)

# Definindo a função "diminuir"
def diminuir(preço=0, taxa=0, formato=False):
    """
    Cálculo a diminuição de um preço em função de uma taxa (%).
    :param preço: preço informada para o cálculo.
    :param taxa: taxa (%) informada que será aumentada no preço.
    :param formato: se False - resultado não formatado, se True - resultado formatado.
    :return: retorna o resultado do cálculo.
    """
    res = preço - ((preço * taxa) / 100)
    # Se não informar "True", ele mostra o resultado sem formatação
    return res if formato is False else moeda(res)

# Definindo a função "dobro"
def dobro(preço=0, formato=False):
    """
    Cálcula o dobro de um preço.
    :param preço: preço informado para o cálculo.
    :param formato: se False - resultado não formatado, se True - resultado formatado.
    :return: retorna o resultado do cálculo.
    """
    res = preço * 2
    return res if not formato else moeda(res)

# Definindo a função "metade"
def metade(preço=0, formato=False):
    """
    Cálcula a metade de um preço.
    :param preço: preço informado para o cálculo.
    :param formato: se False - resultado não formatado, se True - resultado formatado.
    :return: retorna o resultado do cálculo.
    """
    res = preço / 2
    return res if not formato else moeda(res)

# Definindo a função "moeda"
def moeda(preço=0, moeda='R$'):
    """
    Função para formatar o resultado dos cálculos.
    :param preço: preço informado para o cálculo.
    :param moeda: formata o resultado incluindo "R$" no início do resultado.
    :return: retorna o resultado formatado.
    """
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
