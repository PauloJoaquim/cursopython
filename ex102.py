#Paulo, assisti o resultado para poder concluir, estou tendo um pouco de dificuldades no def, ams ja aproveitei e dei um incrementada
def fatorial(valor, show=True):
    f = 1
    for c in range(valor, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

n = int(input('Quer ver o fatorial de qual número: '))
conta = str(input('Quer ver a conta? [S/N] ')).strip().upper()[0]
while conta not in 'SN':
    conta = str(input('Quer ver a conta? [S/N] ')).strip().upper()[0]
if conta == 'N':
    print(fatorial(n, show=False))
else:
    print(fatorial(n, show=True))

#Guanabara
'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial  de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta
    :return: O valor do fatorial de um  número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


#Programa principal
print(fatorial(5, show=True))
help(fatorial)
'''