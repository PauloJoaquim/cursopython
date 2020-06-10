lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

'''EXEMPLOS DE FATIAMENTOS COM TUPLAS'''

#TUPLAS SÃO IMUTAVEIS

#print(lanche[-3])
#mostra de trás para frenete

#print(lanche[1:3])
#qpenas suco e pizza que são os elementos 1 e 2

#print(lanche[1:])
#Do elemento em questão até o final da Tupla

#print(lanche[:2])
#Do inicio até o elemento 2, não considere o elemento em questão

#print(lanche[-3:])
#Vai do elemento -2 até o final

#EXEMPLO DE ==LEN== contagem de str
#print(len(lanche))

#EXEMPLO 1 de  ==FOR==
#for comida in lanche:
    #print(f'Eu vou comer {comida}')

#EXEMPLO 2 de ==FOR== este exemplo será o mesmo resultado dp EXEMPLO 3 ==FOR==
#for cont in range(1, len(lanche)):
    #print(cont)
    #mostra apenas até a posição 3 ou seja até PIZZA

#EXEMPLO 3 de ==FOR==  este exemplo será o mesmo resultado do EXXEMPLO 1 ==FOR==
#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]}')


#EXEMPLO 4 de ==FOR==
#for posição, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {posição}')


#EXEMPLO PARA ORDEM ALFABÉTICA
#for c in sorted(lanche):
    #print(c)
'''ou'''
#print(sorted(lanche))


#EXEMPLOS POR NÚMEROS:
#=====EXEMPLO 01=====UTILIZANDO +
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c)
'''não vai somar e sim juntar as TUPLAS'''

#=====EXEMPLO 02=====UTILANDO count
#print(c.count(5))
'''vai contar quantos há números há na variavel dogitada, 5 foi exemplo pode ser digitado qualquer outro, até mesmo utilizar um input quando for em um banco de dados a ser pesquisado!'''

#=====EXEMPLO 03=====UTILIZANDO index
#print(c)
#print(c.index(8))
'''mostra em qual posição está o número pesquisado, pode ser utilizado tambem através de um input quando for em um banco de dados a ser pesquisadp'''

#=====EXEMPLO 04=====UTILIZANDO del
'''TUPLAS não tem como alterar, mas pode ser deletada'''
pessoa = ('Paulo', 26, 'M', 68.200)
del(pessoa)
print(pessoa)