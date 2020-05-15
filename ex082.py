#Paulo
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista PAR é {par}')
print(f'A lista IMPAR é {impar}')

#Guanabara
'''num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-'*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'a lista de impares é {impares}')'''

