#PAULO - OK
'''contidade = conthomem = contmulher20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    continua = str(input('Quer continuar [S/N]? ')).upper().strip()
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F':
        if idade < 20:
            contmulher20 += 1
    if continua == 'N':
        break

if contidade > 1:
    print(f'Há {contidade} pessoas maior de 18 anos.')
else:
    print(f'Há {contidade} pessoa maior de 18 anos.')
if conthomem > 1:
    print(f'Foram cadastrados {conthomem} homens.')
else:
    print(f'Foi cadastrado {conthomem} homem.')
if contmulher20 > 1:
    print(f'Foram cadastradas {contmulher20} mulheres com menos de 20 anos.')
else:
    print(f'Foi cadastrada {contmulher20} mulher com menos de 20 anos.')'''

#GUANABARA
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Toatl de pessoas com mais de 18 anos é de {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
