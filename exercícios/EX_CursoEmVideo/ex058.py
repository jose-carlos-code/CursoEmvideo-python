import random
acertou = False
tent = 0
computador = random.randint(0,10)
print('pensei em um numero, qual voce acha que eu pensei?')
while not acertou:
    jogador = int(input('qual o seu palpite?: '))
    tent += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais... tente mais uma vez')
        elif jogador > computador:
            print('menos... tente mais uma vez')
print('parabens voce acertou')
print('voce tentou {} vezes ate acertar'.format(tent))
