#Paulo
from time import sleep
valores = []
continuar = procura = ''
lista = valores
while True:
    n = int(input('Digite um valor: '))
    print('Analisando valor...')
    sleep(1)
    if n in valores:
        print('\033[1;31mO valor não pode ser adicionado, pois o mesmo ja consta na lista de valores digitados!\033[m')
    else:
        print('\033[1;36mAdicionado com sucesso!\033[m')
        valores.append(n)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite corretamente! Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*50)
print(f'Os valores digitados foram: {sorted(valores)}')

#Guanabara
'''números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('=-'*30)
números.sort()
print(f'Você digitou os valores {números}')'''
