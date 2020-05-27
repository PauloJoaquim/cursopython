from time import sleep
def contador(inicio, fim, cont):
    print(f'contagem de {inicio} até {fim} contando de {cont} em {cont}')
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


#em andamento
contador(1, 10, 1)
contador(10, 0, 2)