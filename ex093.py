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
