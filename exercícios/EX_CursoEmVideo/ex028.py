import random
p = random.randint(0, 5)
n = int(input('ola usuario, eu pensei em um numero ente 0 e 5, vc conseque descobrir qual e ? digite a sua hipotese: '))
if p == n:
    print ('meus parabens, voce acertou! o numero que pensei foi {}'.format(p))
else:
    print ('ah que pena, voce errou, o numero que pensei foi {}, tente de novo!'.format(p))
