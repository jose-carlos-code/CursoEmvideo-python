valores = list()
for c in range(1, 8):
    valores.append(int(input(f'digite o {c} valor: ')))
print(f'os numeros pares são: ', end=' ')
valores.sort()
for pos, v in enumerate(valores):
    if valores[pos] % 2 == 0:
         print(f'{valores[pos]}', end=' ')
print()
print(f'os números ímpares são: ', end=' ')
for pos, v in enumerate(valores):
    if valores[pos] % 2 != 0:
        print(f'{valores[pos]}', end=' ')
