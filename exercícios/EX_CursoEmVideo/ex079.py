from time import sleep
valores = list()
continuar = ' '
print('-='*15, 'PROGRAMA: NUMEROS ALEATORIOS!', '-='*15)
while continuar != 'n':
    num = int(input('digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado, escolha outro...')
    continuar = str(input('quer continuar[s/n]?: ')).lower()
valores.sort()
print('finalizando...')
sleep(1.5)
print('-='*30)
print(f'os valores digitados foram {valores} ')
print('-='*30)