#PAULO, não feito corretamente condição de parada
'''n = cont = 0
while True:
    n = int(input('Digite um valor para saber sua tabuada ou digite -1 para parar: '))
    if n == -1:
        break
    else:
        cont += 1
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
if cont > 1:
    print(f'Você pesquisou {cont} vezes a tabuadas antes de encerrar')
else:
    print(f'Você pesquisou {cont} vez a tabuada antes de encerrar.')'''

#GUANABARA
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA DE TAUADA ENCERRADO. Volte sempre')