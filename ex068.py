#PAULO
'''from random import choice
números =  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
cont = 0
while True:
    cont += 1
    ncomputador = choice(números)
    njogador = int(input('Digite um valor de 0 a 10: '))
    tjogador = str(input('Digite [I] para impar ou [P] para par')).strip().upper()
    soma = ncomputador + njogador
    resultado = soma % 2
    if resultado == 0:
        resultado = 'P'
    elif resultado == 1:
        resultado = 'I'
    if tjogador == resultado:
        if cont > 1:
            print(f'Parabéns! a soma foi de {soma}, você já ganhou {cont} vezes, você escolheu {tjogador} e o resultado foi {resultado}!!!')
        if cont <= 1:
            print(f'Parabéns! a soma foi de {soma, }você já ganhou {cont} vez, você escolheu {tjogador} e o resultado foi {resultado}!!!')
    else:
        if cont > 1:
            print(f'você perdeu! A soma foi de {soma} você escolheu {tjogador} e o resultado foi {resultado}')
            break
        elif cont <=1:
            print(f'Você perdeu! A soma foi de {soma} você escolheu {tjogador} e o resultado foi {resultado}')
            break
print('-'*30)
print('GAME OVER')
print('-'*30)'''

#GUANABARA
from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor de 1 a 10 '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
if v > 1:
    print(f'GAMER OVER, você venceu {v} vezes.')
elif v == 1:
    print(f'GAMER OVER, você venceu {v} vez.')
else:
    print('GAMER OVER, você não venceu nenhuma vez! Mais sorte na próxima')
