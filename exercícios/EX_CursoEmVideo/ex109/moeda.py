def metade(numero, form=False):
    n = numero/2
    if form == True:
      return moeda(n)
    else:
        return n


def dobro(num,form=False):
    n = num*2
    if form == True:
        return moeda(n)
    else:
        return n


def aumentar(valor, p=0, form=False):
    a = (valor*p)/100
    n = valor+a
    if form == True:
        return moeda(n)
    else:
        return n


def diminuir(numero, p=0, form=False):
    a = (numero*p)/100
    n = (numero - a)
    if form == True:
        return moeda(n)
    else:
        return n


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
