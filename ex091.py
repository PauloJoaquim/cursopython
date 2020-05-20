#Paulo = Faltou colocar em ordem! (Ranking)
from random import randint
dados = dict()
maior = 0
for c in range(1, 5):
    dados[f'Jogador {c}'] = randint(1, 6,)
print(f'O jogador 1 tirou {dados["Jogador 1"]}\n'
      f'O jogador 2 tirou {dados["Jogador 2"]}\n'
      f'O jogador 3 tirou {dados["Jogador 3"]}\n'
      f'O jogador 4 tirou {dados["Jogador 4"]}')
print('Ranking dos jogadores:')
