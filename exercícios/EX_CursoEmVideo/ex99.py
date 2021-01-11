from time import  sleep
def maior(*num):
    cont = m = 0
    print('-='*30)
    print('ANALISANDO OS VALORES PASSADOS....')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.25)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                valor = m
        cont += 1
    print(f'foram informados {cont} valores ao todo')
    print(f'o maior valor informado foi {m}')


maior(2,0,1)
maior(10,20,45,0)
maior()
