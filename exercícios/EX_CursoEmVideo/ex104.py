def leiaInt(num):
    while True:
        numero = input(num)
        if numero.isnumeric():
            return int(numero)
            break
        print('ERRO! digite um número inteiro válido!')


programa princial
n = leiaInt('digite número: ')
print(f'você acabou de digitar o número {n}')
