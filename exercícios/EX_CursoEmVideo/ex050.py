s = 0
for c in range (1, 7):
    n = int(input('me diga um numero: '))
    if n%2 == 0:
     s += n
print('a soma de todos os numeros pares é {}'.format(s))