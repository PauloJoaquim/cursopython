#Paulo = Assisti a solução para fazer, mas não tive dificuldades, achei interessante implementar um pouco no exercício
from ex109 import moeda
r = float(input('Digite um valor R$ '))
a = int(input('Deseja aumentar o valor em quanto? (%) '))
d = int(input('Deseja diminuir o valor em quanto? (%)  '))
while True:
    p = str(input('Quer mostrar os valores formatados? [S/N] ')).strip().upper()[0]
    while p not in 'SN':
        p = str(input('Resposta inválida! Quer mostrar os valores formatados? [S/N] ')).strip().upper()[0]
    if p == 'S' or p == 'N':
        break

if p == 'S':
    print(f'O valor do produto é de {moeda.moeda(r)} o aumento foi de {a}% ficando um total de {moeda.aumentar(r, a,True)}')
    print(f'O valor do produto é de {moeda.moeda(r)} a redução foi de {d}% ficando um total de {moeda.diminuir(r, d,True)}')
    print(f'O dobro de R$ {moeda.moeda(r)} é {moeda.dobro(r, True)}')
    print(f'A metade de R$ {moeda.moeda(r)} é {moeda.metade(r, True)}')

else:
    print(f'O valor do produto é de {moeda.moeda(r)} o aumento foi de {a}% ficando um total de {moeda.aumentar(r, a)}')
    print(f'O valor do produto é de {moeda.moeda(r)} a redução foi de {d}% ficando um total de {moeda.diminuir(r, d)}')
    print(f'O dobro de {moeda.moeda(r)} é {moeda.dobro(r)}')
    print(f'A metade de {moeda.moeda(r)} é {moeda.metade(r)}')


#Guanabara
'''from ex109 import moeda
p = float(input('Digite o preçp: R$ '))
print(f'A metade de {moeda.moeda(p)} é R$ {moeda.metade(p, True)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')'''
