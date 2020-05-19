#Paulo
linha1 = []
linha2 = []
linha3 = []
matriz = []
for c in range(0, 3):
    linha1.append(int(input(f'Digite um valor para linha 0 coluna {c}: ')))
matriz.append(linha1[:])
linha1.clear()
for c in range(0, 3):
    linha2.append(int(input(f'Digite um valor para linha 1 coluna {c}: ')))
matriz.append(linha2[:])
linha2.clear()
for c in range(0, 3):
    linha3.append(int(input(f'Digite um valor para linha 2 coluna {c}: ')))
matriz.append(linha3[:])
linha3.clear()
for c in range(0, 3):
    print(f'[{matriz[0][c]: ^8}]',end='')
print()
for c in range(0, 3):
    print(f'[{matriz[1][c]: ^8}]', end='')
print()
for c in range(0, 3):
    print(f'[{matriz[2][c]: ^8}]',end='')

#Guanabara
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha   in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}], [{coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()'''