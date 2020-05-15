#Paulo
valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
if cont > 1:
    print(f'Foram digitados ao todo {cont} valores!')
else:
    print(f'Foi digitado ao todo {cont} valor!')
valores.sort(reverse=True)
print(f'Os valores digitados foram {valores}')
if 5 in valores:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não foi digitado, portanto não esta na lista!')

#Guanabara
'''valores = []
while True:
    valores.append(int(input('Digite um valor ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=-'*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valo 5 não foi encontrado na lista!')'''
