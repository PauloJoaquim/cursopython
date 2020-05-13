#Não consegui fazer sozinho, necessário estudar esse tipo de exercício!
valor = int(input('Qual valor deseja sacar: R$ '))
cédula = 100
total = valor
contcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        contcéd += 1
    else:
        if contcéd > 0:
            print(f'Toatal de \033[1;34m{contcéd}\033[m de notas de R$ {cédula}')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 2
        elif cédula == 2:
            cédula = 1
        contcéd = 0
        if total == 0:
            break
#Código praticamente copiado do GUANABARA!