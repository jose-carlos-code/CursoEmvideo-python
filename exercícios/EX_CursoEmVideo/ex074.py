from random import randint
numeros = (randint(0, 9), randint(0, 9), randint(0, 9),
           randint(0, 9), randint(0, 9))
print('os numeros sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\no maior valor foi {max(numeros)}')
print('o menor valor foi {}'.format(min(numeros)))
