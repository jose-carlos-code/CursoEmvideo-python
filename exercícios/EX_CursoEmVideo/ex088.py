from time import sleep
from random import randint
cont = 0
jogo = []
quantidade = int(input('quantos jogos você quer que eu sorteie?: '))
for c in range(1, quantidade+1):
    while cont !=6:
        sorteio = randint(1, 60)
        if sorteio in jogo:
            cont += 0
        else:
            jogo.append(sorteio)
            cont += 1
    jogo.sort()
    sleep(0.3)
    print(f'jogo {c}: {jogo}')
    jogo.clear()
    cont = 0
print('BOA SORTE')