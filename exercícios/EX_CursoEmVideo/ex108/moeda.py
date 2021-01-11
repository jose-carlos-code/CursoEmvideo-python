def metade(numero):
    n = numero/2
    return n


def dobro(num):
    n = num*2
    return n


def aumentar(valor, p=0):
    a = (valor*p)/100
    n = valor+a
    return n


def diminuir(numero, p=0):
    a = (numero*p)/100
    n = (numero - a)
    return n

def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
