def metade(numero):
    n = numero/2
    return n


def dobro(num):
    n = num*2
    return n


def aumentar(valor, p=0):
    a = (valor*p)/100
    n = (f'{valor+a:.2f}')
    return n


def diminuir(numero, p=0):
    a = (numero*p)/100
    n = (f'{numero - a:.2f}')
    return n