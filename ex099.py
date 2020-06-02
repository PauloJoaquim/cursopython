#Paulo, precisei assistir para fazer, mas fiz sem problemas, pois estava fazendo utilizando lista
from time import sleep


def maior(*números):
    maior = 0
    cont = 0
    print('-='*20)
    print(f'Analisando os valores informados...')
    sleep(0.5)
    for c in números:
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
        cont += 1
    print(f'-> Foram informados ao todo {cont} números')
    print(f'O \033[1mmaior\033[m valor informado foi \033[1;36m{max(números)}\033[m')
    print(f'E o \033[1mmenor\033[m valor informado foi \033[1;31m{min(números)}\033[m')
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)

#Guanabara
'''from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''