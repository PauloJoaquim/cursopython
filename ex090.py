#Paulo
dados = dict()
média = 0
for c in range(0, 1):
    dados['Nome'] = str(input('Nome: ')).strip().title()
    dados['Média'] = float(input(f'Média de {dados["Nome"]} '))
    if dados['Média'] >= 7:
        dados['Situação'] = '\033[1;34mAprovado\033[m'
    else:
        dados['Situação'] = '\033[1;31mReprovado\033[m'
print(f'O nome é igual a {dados["Nome"]}\n'
      f'Média é igual a {dados["Média"]}\n'
      f'Situação é igual a {dados["Situação"]}')