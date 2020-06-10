#========== EXEMPLO 01 ===== Interactive help =====
help(print())
# ou

print(input.__doc__)

#========== EXEMPLO 02 ===== docstrings =====
def soma(a, b, c):
    """
    --> Faz a soma de três valores e mostra o resultado na tela.
    :param i: Primeiro valor
    :param f: Segundo valor
    :param p: Terceiro valor
    :return: Sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')

soma(3, 2, 5)

#========== EXEMPLO 03 ===== Parametros opcionais =====
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
# ou
soma(b=4, c=2) # pode ser indormado tambem em fora de ordem!

#========== EXEMPLO 03 ===== Escopo de variáveis =====
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale n1')
#ou utilizar a função globals
globals(n1)#desta forma mesmo que tente alterar o valor será o mesmo para todos os chamados!

#========== EXEMPLO 03 ===== Retorno de valores =====
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2} e {r3}') #desta forma não é necessário repetir uma frase de print e sim apenas os valores

#========== EXEMPLO 04 ==========
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

#========== EXEMPLO 05 ==========
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
