pos = 0
valores = list()
for v in range(1, 5+1):
    pos += 1
    valores.append(int(input(f'digite o valor na posição {pos}: ')))
print(f'\nvocê digitou os valores {valores}')
print(f'\no maior valor foi {max(valores)}')
print(f'\no menor valor digitado foi {min(valores)}')
