#Paulo, não consegui colocar os dois ultimos critérios solicitados pelo desafio, vou assistir aula para poder finalizar!
pessoas = dict()
dados = list()
somapessoas = somaidade = média =0
while True:
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
if sexo == 'F':
    print('As mulheres cadastradas foram: ',end='')