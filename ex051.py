t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
décimo = t + (10 - 1) * r
for c in range(t, décimo+r, r):
    print(c,end=' - ')
print('Ok! acabou')