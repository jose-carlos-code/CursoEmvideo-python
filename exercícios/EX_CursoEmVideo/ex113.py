def leiaInt(num):
    while True:
        try:
            numero = int(input(num))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('o usuario preferiu não informar os dados')
            return 0
        else:
            return numero


def leiafloat(num):
    while True:
        try:
            numero = float(input(num))
        except KeyboardInterrupt:
            print(f'o usuário preferiu não informar os dados')
            return 0
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um número real válido!\033[m')
            continue
        else:
            return numero
            break



n1 = leiaInt('digite um numero inteiro: ')
n2 = leiafloat('digite um numero real: ')
print(f'o número inteiro foi {n1} e o número real foi {n2}')