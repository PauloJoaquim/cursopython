contador = 0
soma = 0
média = 0
maior = 0
menor = 0
continuar = ''
N = ''
while continuar != 'N':
    número = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    contador += 1
    soma += número
    média = soma / contador
    if contador == 1:
        maior = número
        menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
print(f'Você digitou {contador} números onde o maoir número digitado foi {maior}, o menor foi {menor}, a soma dos números é de {soma} e a média dos valores é de {média}')