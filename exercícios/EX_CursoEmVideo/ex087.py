pares = somaT = 0
maior = 0
matriz = [[0, 0,0], [0, 0, 0], [0, 0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            pares +=  matriz[l][c]
        if c == 2:
            somaT += matriz[l][c]
        if l == 0:
            maior = matriz[l][c]
        else:
            if l == 1:
                if matriz[l][c] > maior:
                 maior = matriz[l][c]
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*30)
print(f'a soma dos valores pares é {pares}')
print(f'a soma de todos os valores da terceira coluna é {somaT}')
print(f'o maior valor da segunda linha é {maior}')
