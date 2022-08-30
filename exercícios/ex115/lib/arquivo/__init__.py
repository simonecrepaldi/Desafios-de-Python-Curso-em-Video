from ex115.lib.interface import *

# Definindo a função "arquivoExiste" que vai verificar se o arquivo existe
def arquivoExiste(nome):
# Vai tentar abrir o arquivo e na sequência fechá-lo
    try:
        a = open(nome, 'rt')
        a.close()
# Vai dar erro se o arquivo não foi encontrado
    except FileNotFoundError:
        return False
    else:
        return True

# Definindo a função "criarArquivo" para criar o arquivo
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
# Caso ocorra algum problema na criação do arquivo
    except:
        print('Houve um erro na criação do arquivo!')
# Se estiver tudo certo, o arquivo será criado
    else:
        print(f'Arquivo {nome} criado com sucesso!')

# Definindo a função "lerArquivo"
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
# Caso ocorra algum problema na hora de ler o arquivo
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

# Definindo a função "cadastrar"
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
# Caso ocorra um problema na hora de abrir o arquivo
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
# Caso ocorra um problema na hora de cadastrar os dados
        except:
            print('Houve um erro na hora de cadastrar os dados!')
# Se estiver tudo certo, criar novo registro com os dados informados
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
