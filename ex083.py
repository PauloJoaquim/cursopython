#Paulo = precisei assistir solução para fazer, mesmo assim não consegui interder, a lógica sim mas o método não!
expressão = str(input('Digite a expressão: '))
lista = []
for símbolo in expressão:
    if símbolo == '(':
        lista.append('(')
    elif símbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressao está válida!')
else:
    print('Sua expressão está errada!')