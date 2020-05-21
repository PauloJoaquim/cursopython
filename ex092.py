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
