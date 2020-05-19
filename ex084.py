#Paulo
lista = []
dados = []
continuar = ''
contador = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso Kg: ')))
    contador += 1
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*50)
if contador > 1:
    print(f'Ao todo foram cadastradas {contador} pessoas')
else:
    print(f'Foi cadastrada {contador} pessoa')
print('-='*50)
print('As seguintes pessoas pesam a partir de 100kg:')
for pesomaior in lista:
    if pesomaior[1] >= 100:
        print(f'{pesomaior[0]} pesando {pesomaior[1]}kg')
print('-='*50)
print('As seguintes pessoas pesam até 70kg:')
for pesomenor in lista:
    if pesomenor[1] <= 70:
        print(f'{pesomenor[0]} pesando {pesomenor[1]}kg')

#Guanabara
'''temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maio peso foi de {mai}kg. Peso de ', end=' ')
for pessoa in princ:
    if pessoa[1] == mai:
        print(f'[{pessoa[0]}]', end='')
print()
print(f'O menor peso foi de {men}kg', end='')
for pessoa in princ:
    if pessoa[1] == men:
        print(f'[{pessoa[0]}]', end='')
print()'''