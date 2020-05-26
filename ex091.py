#Paulo = Necessário assistir a aula para colocar em ordem
from random import randint
from operator import itemgetter
dados = dict()
maior = 0
for c in range(1, 5):
    dados[f'Jogador {c}'] = randint(1, 6,)
print(f'O jogador 1 tirou {dados["Jogador 1"]}\n'
      f'O jogador 2 tirou {dados["Jogador 2"]}\n'
      f'O jogador 3 tirou {dados["Jogador 3"]}\n'
      f'O jogador 4 tirou {dados["Jogador 4"]}')
print('-='*30)
print('Ranking dos jogadores:')
ranking = dict()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for r in range(1, 5):
    print(f'{r}º {ranking[r-1]}')

#Guanabara
'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)'''