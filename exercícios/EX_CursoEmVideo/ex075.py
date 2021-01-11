numeros = (int(input('digite um numero: ')),
           int(input('digite outro numero: ')),
           int(input('digite mais um numero: ')),
           int(input('digite o ultimo numero: ')))
print(f'os numeros digitados foram {numeros}')
print(f'o numero 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'o numero 3 aparece pela primeria vez na posição {numeros.index(3)+1}')
else:
    print('o numero 3 nao esta em nenhuma posição')
print(f'os numeros pares são', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
