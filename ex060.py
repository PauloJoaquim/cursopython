n = int(input('digite um número para saber seu fatorial: '))
c = n
f = 1
print(f'Calculando fatorial de {n}!',end=' ')
while c > 0:
    print(f'{c}',end='')
    if c > 1:
        print(f' x ',end='')
    else:
        print(' = ',end='')
    f = f * c
    c -= 1
print(f'{f}')