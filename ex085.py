#Paulo
lista = []
pares = []
impares = []
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(sorted(pares[:]))
pares.clear()
lista.append(sorted(impares[:]))
impares.clear()
print(f'Os valores PARES digitados foram {lista[0]}')
print(f'Os valores IMPARES digitados foram {lista[1]}')