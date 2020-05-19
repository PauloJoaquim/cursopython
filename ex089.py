#Paulo
lista = []
variavel = []
notas = []
while True:
    nome = str(input('Nome: ')).strip().title()
    variavel.append(nome)
    nota1 = float(input('Nota 1: '))
    notas.append(nota1)
    nota2 = int(input('Nota 2: '))
    notas.append(nota2)
    variavel.append(notas[:])
    notas.clear()
    média = (nota1 + nota2) / 2
    variavel.append(média)
    lista.append(variavel[:])
    variavel.clear()
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Tente novamente, quer continuar? [S/N]: '))
    if cont == 'N':
        break
print('-='*30)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>10}')
print('-'*50)
for i, r in enumerate(lista):
    print(f'{i:<5}{r[0]:<10}{r[2]:>10.1f}')
print('-'*50)
while True:
    pergunta = int(input('Quer ver as notas de qual aluno? (999 interrompe a busca!): '))
    if pergunta == 999:
        break
    if pergunta <= len(lista) - 1:
        print()
        print(f'Notas do aluno(a) \033[1;34m{lista[pergunta][0]}\033[m são \033[1;34m{lista[pergunta][1]}\033[m')
        print()
print()
print(f'{"="*10}{"VOLTE SEMPRE"}{"="*10}')

#Guanabara
'''ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input(('Nota 2: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')'''