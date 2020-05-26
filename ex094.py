#Paulo, não consegui colocar os dois ultimos critérios solicitados pelo desafio, precisei assistir solução para comclusão, mas percebi que não estava conseguindo porque estava utilizando das formas corretas porem na ordem errada!
pessoas = dict()
dados = list()
somapessoas = somaidade = média =0
while True:
    pessoas.clear()
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Tente novamente. Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    pessoas['Nome'] = nome
    pessoas['Sexo'] = sexo
    pessoas['Idade'] = idade
    dados.append(pessoas.copy())
    somapessoas += 1
    somaidade += idade
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*50)
print(f'- O grupo tem {somapessoas} pessoas.')
média = somaidade / somapessoas
print(f'- A média de idade é de {média:.2f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for p in dados:
    if p['Sexo'] in 'F':
        print(p['Nome'], end=' ')
print()
print('- A lista de pessoas que estão acima da média são:',end=' ')
for p in dados:
    if p['Idade'] >= média:
        print(f'{p["Nome"]} com a idade de {p["Idade"]} anos',end=', ')
print()
print(' << ENCERRADO >>  ')

#Guanabara
'''galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulherer cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ',end='')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('  ENCERRADO >>  ')'''
