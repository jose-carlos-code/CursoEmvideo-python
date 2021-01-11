import random
from time import sleep
from operator import  itemgetter
maior = menor = contador = 1
num = dict()
numero1 = random.randint(1, 6)
num['jogador 1 '] = numero1
numero2 = random.randint(1, 6)
num['jogador 2'] = numero2
numero3 = random.randint(1, 6)
num['jogador 3'] = numero3
numero4 = random.randint(1,6)
num['jogador 4'] = numero4
for k, v, in num.items():
    print(f'o {k} tirou {v}')
print('RANKING DOS JOGADORES: ')
dic = (sorted(num.items(), key=itemgetter(1), reverse=True))
for k, v in dic:
    sleep(1)
    print(f'em {contador} lugar: {k} com {v}')
    contador+= 1