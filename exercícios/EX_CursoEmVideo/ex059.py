from time import sleep
print('--------- MENU DE CARLOS ----------')
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor :'))
maior = 0
q = 0
while q != 5:
    print('========  --- ========')
    print('''
    [1] para somar
    [2] para multiplicar
    [3] saber qual é o maior
    [4] novos numeros
    [5] sair do programa''')
    print('========  --- ========')
    q = int(input('>>>>>>>>>>> digite aqui: '))
    if q == 1:
        print('a soma entre {} e {}  é {}'.format( n1, n2, n1 + n2))
    elif q == 2:
        print('a multiplicação entre {} {}  é {}'.format(n1, n2, n1 * n2))
    elif q == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print('o numero maior é {}'.format(maior))
    elif q == 4:
        print('>>>>>>>>>>> digite novos numeros')
        n1 = int(input('digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
print('finalizando...')
sleep(1.5)
print('fim do programa. obrigado, volte sempre!')
