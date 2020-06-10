#==========EXEMPLO 01==========
'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])#Se não coolocar [:] a alteração não irá ocorrer
teste[0] = 'Maria' #alterando do nome GUSTAVO para o nome MARIA
teste[1] = 22 #Alterando da idade 40 para idade 22
galera.append(teste[:]) #Se não coolocar [:] a alteração não irá ocorrer (tem como função criar uma cópia
print(galera)'''

#==========EXEMPLO 02==========
'''#            0      1      0     1        0       1       0      1
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#                0           1               2              3
print(galera[0]) #mostra [JOÃO, 19]
print(galera[0][0]) #mostra JOÃO
print(galera[2][1])#mostra 13
for pessoa in galera:
    #print(pessoa)#vai mostrar na primeira linha: ['JOÃO', 19] segunda linha: ['ANA', 33] e assim sucessivamente!
    #print(pessoa[0])#Vai mostrar apenas os nomes
    #print(pessoa[1])  # Vai mostrar apenas as idades
    #print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')#vai mostrar em ordem nome e idade'''

#==========EXEMPLO 03==========
totalmaior = totalmenor = 0
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalmenor += 1

print(f'Temos {totalmaior} maiores de idade e temos {totalmenor} menores de idade')
