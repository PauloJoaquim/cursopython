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