from random import shuffle
aL1 = str(input('nome do aluno 1: '))
aL2 = str(input('nome do aluno 2: '))
aL3 = str(input('nome do aluno 3: '))
aL4 = str(input('nome do aluno 4: '))
lista = [aL1, aL2,aL3, aL4]
shuffle(lista)
print('a ordem de apresentação será')
print(lista)