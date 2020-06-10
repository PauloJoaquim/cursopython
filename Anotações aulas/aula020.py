#========== EXEMPLO 01 ==========
'''def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)#Vai mostrar apenas os resultados
#ou
soma(a=4, b=5)
soma(a=8, b=9)
soma(a=2, b=1)
soma(a=4, b=1)#Vai mostrar apenas os resultados, mas desta forma está sendo explicito quem é quem'''

#========== EXEMPLO 02 ==========
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#programma principal
soma(4, 5)'''

#========== EXEMPLO 03 ==========
'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

#========== EXEMPLO 04 ==========
'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 5]
dobra(valores)
print(valores)'''

#========== EXEMPLO 05 ==========
def soma(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)