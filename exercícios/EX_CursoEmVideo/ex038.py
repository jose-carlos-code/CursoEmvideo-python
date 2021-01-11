numero1 = int(input('escreva um numero(inteiro): '))
numero2 = int(input('escreva outro numero(inteiro): '))
if numero1 > numero2:
    print('o numero {} é o maior'.format(numero1))
elif numero2 > numero1:
    print('o numero {} é o maior'.format(numero2))
else:
    print('os dois numeros sao iguais. por tanto, nao tem numero maior.')
