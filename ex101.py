#Paulo = OK
'''from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade <= 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


nasc = int(input('Ano de nascimento: '))
voto(nasc)'''

#Guanabara


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))