#foi necessário assistir resolução do problema para conseguir concluir exercício!
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos as seguintes vogais: ',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra.upper(),end=' ')
