#feito, mas imcompleto, faltou nome do produto mais caro
'''total = cont = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('digite o valor do produto R$ '))
    total += preço
    if preço > 1000:
        cont += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('')
print('===== RESULTADO =====')
print(f'O valor total gasto é de R$ {total:.2f}')
print(f'O total de produtos de custaram acima de R$ 1000.00 foi de {cont}')'''

#GUANABARA
total = totmil = menor = cont= 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O valor total é de R$ {total:.2f}')
print(f'Temos {totmil} produtos que custaram mais de R$ 1000.00')
print(f'O produto mais barato foi {barato}, custando R$ {menor:.2f}')