import time
c = (   '\033[m',          # 0 - sem cores
        '\033[0;30;41m',   # 1 - vermelho
        '\033[0;30;42m',   # 2 - verde
        '\033[0;30;43m',   # 3 - amarelo
        '\033[0;30;44m',   # 4 - azul
        '\033[0;30;45m',   # 5 - roxo
        '\033[7;30m',   # 6 - branco
)
def ajuda(com):
    titulo(f'acessando o manual do comando \'{com} \'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    time.sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(F'    {msg}')
    print('~'*tam)
    print(c[0], end='')
    time.sleep(1)


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDAD PYHELP', 2)
    comando = str(input('função ou biblioteca >  '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FINALIZANDO...', 6)
time.sleep(1.3)
titulo('FIM DO PROGRAMA', 2)