#Paulo
valores = []
for c in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {max(valores)} na {valores.index(max(valores))}ª posição')
print(f'O menor valor digitado foi {min(valores)} na {valores.index(min(valores))}ª posição')

#Guanabara
'''listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições',end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ',end='')
print()'''
