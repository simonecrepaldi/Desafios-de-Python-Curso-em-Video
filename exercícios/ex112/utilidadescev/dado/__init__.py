# Definindo a função "leiaDinheiro"
def leiaDinheiro(msg):
    válido = False
    while not válido:
# Se digitar "," no preço, ele converte (replace) para "." e já tira (strip) os espaços em branco
        entrada = str(input(msg)).replace(',', '.').strip()
# Se não for numérico ou se não digitar nada, vai informar erro
        if entrada.isalpha() or entrada == '':
            print(f'\033[1:31mERRO: {entrada} não é um preço válido!\033[m')
        else:
            válido = True
            return float(entrada)
