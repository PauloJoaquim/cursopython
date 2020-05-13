bancodados = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
número = int(input('Digite um número entre 0 e 20: '))
while número not in range(0, 21):
    número = int(input('Tente novamente, digite um número entre 0 e 20: '))
print(f'Você digitou o número {bancodados[número]}')
