#Paulo
from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano
carteira = int(input('Digite o número da carteira de trabalho ou digite 0 se não tiver: '))
dados['CTPS'] = carteira
if carteira != 0:
    contratação = int(input('Ano de contratação: '))
    dados['Contratação'] = contratação
    contribuiu = date.today().year - contratação
    deve = 35 - contribuiu
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + deve
for c, v in dados.items():
    print(f'{c} tem o valor {v} ')

#Guanabara
'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aponsentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')'''
