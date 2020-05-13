#PAULO
continuar = ' '
cont = 0
bancodados = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    número = ' '
    while número not in range(0, 21):
        número = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {bancodados[número]}')
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('='*15)
if cont == 1:
    print(f'Você digitou número por {cont} vez!')
else:
    print(f'Você digitou número por {cont} vezes!')
print('='*15)


#GUANABARA
'''cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamnete. ',end='')
print(f'Você digitou o número {cont[número]}')'''