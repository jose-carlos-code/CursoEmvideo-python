def leiadinheiro(msg):
    """
    formata um valor(em dinheiro) com as características do REAL
    :param msg: recebe a string
    :return: retorna o numero float
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace('.',',').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)

def leiaInt(num):
    """
    função que verifica se um numero é inteiro
    ou não.
    :param num: recebe uma string
    :return: a variável 'numero', que é convertido para um numero inteiro
    """
    while True:
        try:
            numero = int(input(num))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! digite um número inteiro válido!\033[m')
            continue
        else:
            return numero


def cores(nome):
    """
    função para colori os textos mais facilmente.
    :param nome: recebe o nome da cor
    :return: o codigo da cor que está dentro de um dicionário, através da variavel 'v'
    """
    cor = dict()
    cor = {'padrao': '\033[m', 'vermelho':'\033[31m', 'branco':'\033[30m',
           'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m',
           'roxo': '\033[35m', 'azul02':'\033[36m', 'cinza':'\033[37m'}
    for k, v in cor.items():
        if nome == k:
            return v