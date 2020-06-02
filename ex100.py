#Paulo = copiei o exercio, assiti duas vezes e não consegui interder a solução, assitirei novamente a aula 20 para tentar intender
from random import randint
from time import sleep


def sorteio(lista):
    print('sorteando 5 valores da lista: ',end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Soamndo is valores pares de {lista}, temos {soma}')


números = list()
sorteio(números)
sorteio(números)
