# Importando os arquivos
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

# Verificando se "arq" existe, se não existir , criar "arq"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
# Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
# Opção de cadastrar uma nova pessoa.
       cabeçalho('NOVO CADASTRO')
       nome = str(input('Nome: '))
       idade = leiaInt('Idade: ')
       cadastrar(arq, nome, idade)
    elif resposta == 3:
# Opção de sair do sistema.
       cabeçalho('Saindo do sistema... Até logo!')
    else:
       print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
