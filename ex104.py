#Paulo = precisei assistir solução, mas consegui elaborar outro método utilizando menos memória!
def leiaInt(valor):
    while True:
        n = str(input(valor))
        if n.isnumeric():
            n = n
            break
        else:
            print('\033[1;31mERRO!\033[m \033[0;31mDigite um número inteiro válido.\033[m')
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


#Guanabara
'''def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO!\033[m \033[0;31mDigite um número inteiro válido.\033[m')
        if ok:
            break
        return valor


n = leiaInt('digite um número: ')
print(f'Você acabou de digitar o número {n}')
'''