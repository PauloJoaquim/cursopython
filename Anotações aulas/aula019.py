#==========EXEMPLO 01==========
'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(pessoas['nome']) #Mostra apenas GUSTAVO'''

#==========EXEMPLO 02==========
'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')#mostra: O Gustavo tem 22 anos'''

#==========EXEMPLO 03==========
'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(pessoas.keys())#Vai mostra as chaves ou seja (nome, sexo e idade)
print(pessoas.values())#Vai mostrar os valores: (gustavo, M e 22)
print(pessoas.items())#Vai mostrar tudo'''

#==========EXEMPLO 03==========
'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}

pessoas['nome'] = 'Leandro' #O nome de GUSTAVO passa a ser LEANDRO

pessoas['Peso'] = 98.5 #Desta forma foi adiciobnado peso ao dicionario

del pessoas['Sexo']#apagando o sexo automaticamente o mesmo não irá aparecer no print a seguir!

for k, v in pessoas.items():
    print(f'{k} = {v}') #Vai mostrar (Nome = gustavo) e assim sucessivamente!'''

#==========EXEMPLO 04==========
'''brasil = list()
estado1 = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['Uf'])#Vai mostrar 'Rio de Janeiro'

print(brasil[1]['Sigla'])#Vai mostrar 'SP'

print(brasil)#Vai mostrar o dicionario inteiro'''

#==========EXEMPLO 05==========
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())#Utilizar o ".copy" para mesclar o dicionario com a lista, mesma função do "[:]"
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()