#Não consegui fazer os números pares
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')
cont9 = 0
if n1 == 9:
    cont9 += 1
if n2 == 9:
    cont9 += 1
if n3 == 9:
    cont9 +=1
if n4 == 9:
    cont9 += 1
if cont9 == 0:
    print(f'O valor 9 não apareceu nenhuma vez')
elif cont9 == 1:
    print(f'O valor 9 apareceu {cont9} vez')
elif cont9 > 1:
    print(f'O valor 9 apareceu {cont9} vezes')
if n1 == 3:
    print(f'O primeiro valor 3 foi digitado na 1° posição')
elif n2 == 3:
    print('O primeiro valor 3 foi digitado na 2° posição')
elif n3 == 3:
    print('O primeiro valor 3 foi digitado na 3° posição')
elif n4 == 3:
    print('O primeiro valor 3 foi digitado na 4° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
