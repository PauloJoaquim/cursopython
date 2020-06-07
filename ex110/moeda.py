#Paulo = Assisti a solução para fazer, mas não tive dificuldades


'''def aumentar(valor=0, n=0, formato=False):
    if not formato:
        return (valor / 100) * n + valor
    else:
        return moeda((valor / 100) * n + valor)


def diminuir(valor=0, n=0, formato=False):
    if not formato:
        return valor - (valor / 100) * n
    else:
        return moeda(valor - (valor / 100) * n)

def dobro(n=0, formato=False):
    if not formato:
        return n * 2
    else:
        return moeda(n * 2)


def metade(n=0, formato=False):
    if not formato:
        return n / 2
    else:
        return moeda(n / 2)

def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
'''
#Guanabara


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
