#Paulo, OK
lista = dict()


def notas(*valores, sit=False):
    """
                =========== Função criada para analisar notas e situação de alunos. ==========
    :param valores: uma ou varias notas (aceita quantos valores necessários).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação dos alunos com base nas médias.
    :return: Retorna a quantidade de notas, a maior nota, menor nota e a situação da turma quando optada por ver.
    """
    cont = 0
    cont += len(valores)
    lista['Notas'] = cont
    lista['Maior'] = max(valores)
    lista['Menor'] = min(valores)
    lista['Média'] = sum(valores) / len(valores)
    if sit:
        if lista['Média'] < 5:
            lista['Situação'] = 'RUIM'
        elif lista['Média'] < 7:
            lista['Situação'] = 'RAZOAVEL'
        else:
            lista['Situação'] = 'BOA'
    return lista



resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)


#Guanabara
'''def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas de alunos (aceita várias).
    :param sit: Valor opcioanl, indicando se deve ou não adicionar a situação.
    :return: dicionario com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
'''