import random
aL1 = str(input('nome do aluno 1: '))
aL2 = str(input('nome do aluno 2: '))
aL3 = str(input('nome do aluno 3: '))
aL4 = str(input('nome do aluno 4: '))
lista = [aL1, aL2, aL3, aL4]
s = random.choice(lista)
print('o aluno escolhido foi {}'.format(s))
