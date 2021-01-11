frase = str(input('me diga uma frase qualquer: ')).strip().lower()
print('a letra a aparece {} vezes'.format(frase.count('a')))
print('a letra a aparece pela primeira vez na posição {} '.format(frase.find('a')+1))
print('a letra a aparece pela ultima vez na posição {} '.format(frase.rfind('a')+1))
