#Paulo
dados = dict()
gols = list()
somagols = 0
dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for c in range(0, partidas):
    n = int(input(f'Quantos gols na partida {c}? '))
    gols.append(n)
    somagols += n
dados['Gols'] = gols
dados['Total'] = somagols
print('-='*50)
print(dados)
print('-='*50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*50)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'     => Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {dados["Total"]} gols.')

#Guanabara
'''jogador  = dict()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
partidas = list()
for c in range(0, tot):
    partidas.append(int(input(f'quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''
