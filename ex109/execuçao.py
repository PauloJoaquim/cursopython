#Paulo = Assisti a solução para fazer, mas não tive dificuldades
from ex108 import moeda
r = float(input('Digite um valor R$ '))
a = int(input('Deseja aumentar o valor em quanto? (%) '))
d = int(input('Deseja diminuir o valor em quanto? (%)  '))


print(f'O valor do produto é de {moeda.moeda(r)} o aumento foi de {a}% ficando um total de {moeda.moeda(moeda.aumentar(r, a))}')

print(f'O valor do produto é de {moeda.moeda(r)} a redução foi de {d}% ficando um total de {moeda.moeda(moeda.diminuir(r, d))}')

print(f'O dobro de R$ {moeda.moeda(r)} é {moeda.moeda(moeda.dobro(r))}')

print(f'A metade de R$ {moeda.moeda(r)} é {moeda.moeda(moeda.metade(r))}')
