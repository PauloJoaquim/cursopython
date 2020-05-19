#Paulo - não consegui colocar para não repetir, irei assistir solução do exercício
from random import randint
from time import sleep
lista = []
números = range(1, 61)
print('-='*15)
print(f'{"MEGA SENA": ^30}')
print('-='*15)
p = int(input('Quantos jogos você quer sortear? '))
print(f'-=-=-=-=  SORTEANDO {p} JOGOS  -=-=-=-=')
for c in range(0, p):
    escolhidos = [randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61), randint(1, 61)]
    lista.append(escolhidos)
    print(f'Jggo {c+1}: {sorted(lista[c])}')
    sleep(0.5)
print(f'-=-=-=-=  < BOA SORTE! > -=-=-=-=')
print(f'{"BOA SORTE!" :=^40}')