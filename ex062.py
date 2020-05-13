t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contador = 1
p = 10
total = 0
while p != 0:
    total = total + p
    while contador <= total:
        print(t)
        contador += 1
        t = t + r
    p = int(input('Quantos termos a mais gostaria de mostrar? digite 0 para finalizar! '))
print(f'O total de termos somando-os são {total}')