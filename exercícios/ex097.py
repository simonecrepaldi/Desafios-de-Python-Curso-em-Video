# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Definindo a função "mensagem"
def escreva(mensagem):
# +4 pra deixar uma 'bordinha' antes e depois do texto, além do comprimento da mensagem
    print('-'*(len(mensagem)+4))
    print(f'  {mensagem}')
    print('-'*(len(mensagem)+4))


# Programa Principal
escreva('Olá, Mundo!!!')
escreva('Olá, tudo bem com você?')
escreva('Oi!!!')
