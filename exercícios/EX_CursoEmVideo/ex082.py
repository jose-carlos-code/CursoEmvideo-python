num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('digite um numero: ')))
    resp = str(input('quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-='*30)
print(f'a lista completa é {num}')
print(f'a lsitade pares é {pares}')
print(f'a lista ímpares é {ímpares}')
