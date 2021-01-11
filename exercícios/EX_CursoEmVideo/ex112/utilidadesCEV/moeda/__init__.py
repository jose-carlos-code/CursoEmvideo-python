def divisoria():
    print('=' * 30)


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


def resumo(preço=0, aum=0,redu=0):
    divisoria()
    print(f'{"RESUMO DO VALOR".center(30)}')
    divisoria()
    #coluna da esquerda
    print(f'preço analisado: \t{moeda(preço)}')
    print(f'dobro do preço:  \t{dobro(preço, True)}')
    print(f'metade do preço:  \t{metade(preço, True)}')
    print(f'{aum}% de aumento: \t{aumentar(preço,aum, True)}')
    print(f'{redu}% de redução: \t{diminuir(preço, redu, True)}')
    divisoria()