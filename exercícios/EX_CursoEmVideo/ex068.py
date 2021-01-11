from time import sleep
import random
pc = 0
soma = 0
v = 0
print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-'*30)
while True:
    numero = int(input('qual o seu número?: '))
    pc = random.randint(1,10)
    i = str(input('par ou ímpar?(p/i): '))
    soma = numero + pc
    if i == 'p':
        if soma % 2 == 0:
            print('-' * 30)
            print(f'''voce venceu!
            voce jogou {numero} e o pc {pc} o total é {soma} deu par''')
            print('-' * 30)
            print('vamos jogar novamente...')
            v+=1
        else:
            print('-'*30)
            print(f'PERDEU! voce jogou {numero} e o pc {pc} o total é {soma} deu ímpar')
            print('-'*30)
            break
    elif i == 'i':
        if soma % 2 != 0:
            print('-' * 30)
            print(f'voce venceu! voce jogou {numero} e o pc {pc} o toal é {soma} deu ímpar')
            print('-' * 30)
            v+=1
            print('vamos jogar novamente...')
        else:
            print('-' * 30)
            print(f'PERDEU! voce jogou {numero} e o pc {pc} o total é {soma} deu par')
            print('-' * 30)
            break
print('finalizando...')
sleep(2)
print(f'voce venceu {v} vezes')
print('obrigado por jogar, volte sempre!')
