#PAULO
'''lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*30)
print('     LISTAGEM DE PREÇOS')
print('-'*30)
print(f'{lista[0]}............R$ {lista[1]:.2f}')
print(f'{lista[2]}.........R$ {lista[3]:.2f}')
print(f'{lista[4]}..........R$ {lista[5]:.2f}')
print(f'{lista[6]}...........R$ {lista[7]:.2f}')
print(f'{lista[8]}.....R$ {lista[9]:.2f}')
print(f'{lista[10]}.........R$ {lista[11]:.2f}')
print(f'{lista[12]}..........R$ {lista[13]:.2f}')
print(f'{lista[14]}..........R$ {lista[15]:.2f}')
print(f'{lista[16]}............R$ {lista[17]:.2f}')
print('-'*30)'''

#GUANABARA
print('-'*45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*45)
listagem = ('Lápis', 1.75,
             'Borracha', 2.00,
             'Caderno', 15.90,
             'Estojo', 25.00,
             'Transferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Canetas', 22.30,
             'Livro', 34.90)
for posiçao in range(0, len(listagem)):
    if posiçao % 2 == 0:
        print(f'{listagem[posiçao]:.<30}', end= ' ')
    else:
        print(f'R$ {listagem[posiçao]:.>10.2f}')
print('-'*45)