#Paulo = Precisei assistir mas não tive dificuldades, estava errando em detalhe
def leiadinheiro(valor):
    válido = False
    while not válido:
        n = str(input('Digite o valor: R$ ')).replace(',', '.').strip()
        if n.isalpha():
            print(f'\033[1;31mERRO!\033[m \033[0;31m"{n}" é um valor inválido.\033[m')
        elif n == '':
            print(f'\033[1;31mERRO!\033[m \033[0;31m"{n}" é um valor inválido.\033[m')
        else:
            válido = True
            return float(n)

#Guanabara


'''def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
'''