n = int(input('Digite um número para saber seu fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(f'{c}',end=' ')
    if c > 1:
        print('x',end=' ')
    else:
        print('=',end=' ')
    f *= c
print(f)