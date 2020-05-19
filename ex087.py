#Paulo
linha1 = []
linha2 = []
linha3 = []
matriz = []
somapares = n = somaterceira = 0
maiorvalor = 0
for c in range(0, 3):
    n = int(input(f'Digite um valor para linha 0 coluna {c}: '))
    linha1.append(n)
    if n % 2 == 0:
        somapares += n
matriz.append(linha1[:])
linha1.clear()
for c in range(0, 3):
    n = int(input(f'Digite um valor para linha 1 coluna {c}: '))
    linha2.append(n)
    if n % 2 == 0:
        somapares += n
    if n > maiorvalor:
        maiorvalor = n
matriz.append(linha2[:])
linha2.clear()
for c in range(0, 3):
    n = int(input(f'Digite um valor para linha 2 culuna {c}: '))
    linha3.append(n)
    if n % 2 == 0:
        somapares += n
matriz.append(linha3[:])
linha3.clear()
print('-='*40)
for c in range(0, 3):
    print(f'[{matriz[0][c]: ^8}]',end='')
print()
for c in range(0, 3):
    print(f'[{matriz[1][c]: ^8}]', end='')
print()
for c in range(0, 3):
    print(f'[{matriz[2][c]: ^8}]',end='')
print()
print('-='*40)
print(f'A soma dos valores pares é de {somapares}')
somaterceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é de {somaterceira}')
print(f'O maior valor da segunda linha é {maiorvalor}')

#Guanabara
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha   in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}], [{coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}')'''


