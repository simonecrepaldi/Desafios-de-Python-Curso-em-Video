# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas, - A maior nota, - A menor nota, – A média da turma, – A situação (opcional). Adicionar também docstring.

# Definindo a função "notas"
# Como vai adicionar várias notas (não sabemos quantas) usar '*', já a situação é opcional então recebe 'False'
def notas(*n, sit=False):
# Docstring
    """
    Função para analisar notas e situação de vários alunos.
    :param n: valor de uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação conforme a média dos alunos.
    :return: dicionário com várias informações sobre a situação da turma.
    """
# Criando o dicionário "r"
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
# Verificando a situação do aluno
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
