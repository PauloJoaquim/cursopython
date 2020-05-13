from random import choice
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
escolhidos = (choice(lista), choice(lista), choice(lista), choice(lista), choice(lista))
print(f'Os valores sorteados foram: {escolhidos}')
ordem = sorted(escolhidos)
menor = (ordem[0])
maior = (ordem[4])
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
