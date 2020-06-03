#Não vi necessidade de repetir todo o processo do exercício 106
while True:
    p = str(input('Função ou Biblioteca: '))
    help(p)
    if p.strip().upper() == 'FIM':
        break

print('SISTEMA ENCERRADO!')