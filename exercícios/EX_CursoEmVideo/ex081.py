numeros = []
continuar = ''
while True:
    n = int(input('digite um numero: '))
    numeros.append(n)
    continuar = input('quer continuar?[s/n]: ').lower()
    if continuar in 'Nn':
        break
print(f'o total de numeros digitados foi {len(numeros)}')
numeros.sort(reverse=True)
print(f'a lista em forma decrescente é : {numeros}')
if 5 in numeros:
    print('o numero 5 foi digitado e está na lista')
else:
    print('o numero 5 não foi digitado e não está na lista')
