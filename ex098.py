#Paulo = Solução praticamente cópiada, intendi o exercicio porem tive dificuldades para realizar o memso!
from time import sleep
def contador(inicio, fim, cont):
    print('-='*30)
    print(f'contagem de {inicio} até {fim} contando de {cont} em {cont}')
    if cont < 0:
        cont *= -1
    if cont == 0:
        cont = 1
    if inicio < fim:
        pulo = inicio
        while pulo <= fim:
            print(f'{pulo}',end=' ', flush=True)
            sleep(0.5)
            pulo += cont
        print('FIM!')
    else:
        pulo = inicio
        while pulo >= fim:
            print(f'{pulo}', end=' ', flush=True)
            sleep(0.5)
            pulo -= cont
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem')
início = int(input('Início: '))
final = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, final, passo)
