# Definindo a função "aumentar"
def aumentar(preço=0, taxa=0):
    res = preço + ((preço * taxa)/100)
    return res

# Definindo a função "diminuir"
def diminuir(preço=0, taxa=0):
    res = preço - ((preço * taxa)/100)
    return res

# Definindo a função "dobro"
def dobro(preço=0):
    res = preço *2
    return res

# Definindo a função "metade"
def metade(preço=0):
    res = preço / 2
    return res

# Definindo a função "moeda"
def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
    