#Paulo
dados = dict()
gols = list()
somagols = 0
tot = list()
time = list()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
    for c in range(0, partidas):
        n = int(input(f'Quantos gols na partida {c}? '))
        gols.append(n)
        somagols += n
    tot.append(somagols)
    dados['Gols'] = gols[:]
    dados['Total'] = tot.copy()
    tot.clear()
    time.append(dados.copy())
    gols.clear()
    somagols = 0
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Resposta incorreta, por favoe responder com S para SIM ou N para NÃO')
    if continuar == 'N':
        break
print('-='*50)
print(f'{"Cod.":<5} {"Nome":<8} {"Gols":<15} {"Total":<3}')
for k, v in enumerate(time):
    print(f'{k:<5} {v["Nome"]:<8} {str(v["Gols"]):<15} {str(v["Total"]):<3}')
print('-='*50)
while True:
    busca = int(input('Quer mostrar os gols por partida de qual jogador? (999 encerra o programa) '))
    if busca == 999:
        break
    if busca > len(time)-1:
        print(f'\033[1;31mcódigo inválido\033[m, por favor tente novamente!')
    else:
        print(f' === LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            if g > 1:
                print(f'No jogo {i} fez {g} gols.')
            else:
                print(f'No jogo {i} fez {g} gol.')
print()
print('===== Fim do programa, volte sempe!!! =====')
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
