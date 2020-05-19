#Paulo - não consegui colocar para não repetir, irei assistir solução do exercício
'''from random import randint
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
print(f'{"BOA SORTE!" :=^40}')'''

#Guanabara
from random import randint
from time import sleep
lista = []
jogos = []
print('-='*30)
print('                      JOGA NA MEGA SEMA           ')
print('-='*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS ', '-='*3)
for indice, l in enumerate(jogos):
    print(f'Jogo {indice+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '-='*5)
