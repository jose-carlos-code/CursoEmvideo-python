cont = n = s = 0
while True:
    n = int(input('digite um numero(999 para parar): '))
    if n == 999:
        break
    else:
        cont += 1
        s += n
print(f'o total de numeros digitados foi {cont}')
print(f'a soma entre esses numeros foi {s}')
