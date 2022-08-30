# Definindo a função "aumentar"
def aumentar(preço, taxa):
    res = preço + ((preço * taxa)/100)
    return res

# Definindo a função diminuir
def diminuir(preço, taxa):
    res = preço - ((preço * taxa)/100)
    return res

# Definindo a função "dobro"
def dobro(preço):
    res = preço *2
    return res

# Definindo a função "metade"
def metade(preço):
    res = preço / 2
    return res
