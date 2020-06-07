#Paulo = Assisti a solução para fazer, mas não tive dificuldades


def aumentar(valor=0, n=0):
    return (valor / 100) * n + valor


def diminuir(valor=0, n=0):
    redução = (valor / 100) * n
    return valor - redução


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
