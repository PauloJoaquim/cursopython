import moeda
r = float(input('Digite um valor R$ '))
a = int(input('Deseja aumentar o valor em quanto? (%) '))
d = int(input('Deseja diminuir o valor em quanto? (%)  '))


print(f'O valor do produto é de R${r:.2f} e o aumento foi de {a}% ficando um total de R$ {moeda.aumentar(r, a):.2f}')

print(f'O valor do produto é de R${r:.2f} a redução foi de {d}% ficando um total de R$ {moeda.diminuir(r, d):.2f}')

print(f'O dobro de {r} é {moeda.dobro(r)}')

print(f'A metade de {r} é {moeda.metade(r)}')