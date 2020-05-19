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

#Guanabara
'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')'''