cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont +1
        print(c)
        s = s + c
print('a soma de todos os {} numeros impares multiplos de 3, e que estao entre 1 e 500 é {}'.format(cont, s))