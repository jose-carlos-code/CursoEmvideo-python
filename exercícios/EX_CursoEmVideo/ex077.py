palavras = ('casa', 'comida', 'taxi', 'uber', 'aviao',
            'pyhton', 'java', 'compilador', 'computacao')
for p in palavras:
    print(f'\nna palavra {p} temos as vogais: ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(f'{v}', end=' ')
