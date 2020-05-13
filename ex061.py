t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contador = 1
while contador <= 10:
    print(f'{t}',end=' - ')
    t += r
    contador += 1
