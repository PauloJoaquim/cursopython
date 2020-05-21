#Paulo, vou assistir solução para tentar novamente!
dados = dict()
gols = list()
somagols = 0
while True:
    dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
    for c in range(0, partidas):
        n = int(input(f'Quantos gols na partida {c}? '))
        gols.append(n)
        somagols += n
    dados['Gols'] = gols
    dados['Total'] = somagols
    print('-='*50)