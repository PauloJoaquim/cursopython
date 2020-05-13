cont = soma = 0
while True:
    n = int(input('Digite um número ou digite 999 para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma é de {soma}')
