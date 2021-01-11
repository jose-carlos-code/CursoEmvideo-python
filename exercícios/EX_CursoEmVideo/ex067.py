while True:
    numero = int(input('voce quer ver a tabuada de qual numero?: '))
    print('-'*30)
    if numero < 0:
        break
    for c in range(1, 11):
            print(f'{numero} X  {c} = {numero*c}')
    print('-' * 30)
print('FIM DO PROGRAMA')
print('volte sempre!')