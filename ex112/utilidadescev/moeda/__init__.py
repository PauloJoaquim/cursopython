#Paulo = OK


def aumentar(valor=0, n=0, formato=False):
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


def resumo(valor, a, r):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço análisado:":<20}',end='')
    print(f'{moeda(valor)}')
    print(f'{"Dobro do preço:":<20}', end='')
    print(f'{moeda(dobro(valor))}')
    print(f'{"Metade do preço:":<20}', end='')
    print(f'{moeda(metade(valor))}')
    print(f'{"80% de aumento:":<20}', end='')
    print(f'{moeda(aumentar(valor, a))}')
    print(f'{"35% de redução:":<20}', end='')
    print(f'{moeda(diminuir(valor, r))}')
    print('-'*30)

#Guanabara


'''def aumentar(preço=0, taxa=0, formato=False):
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


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)
'''