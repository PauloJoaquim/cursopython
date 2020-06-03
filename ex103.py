#Deu erro ao deixar input em branco, mas após ver o video a solução não foi dificil!
def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gols no campeonato '


p1 = str(input('Nome do jogador: ')).strip().title()
p2 = str(input('números de gols: '))
if p2.isnumeric():
    p2 = int(p2)
else:
    p2 = 0
if p1 == "":
    p1 = '<Desconhecido>'
print(ficha(p1, p2))


#Guanabara
'''def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogado {jog} fez {gol} gol(s) no campeonato.')


#programa principal
n = str(input('Nome do Jogador: '))
g = str( input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
'''