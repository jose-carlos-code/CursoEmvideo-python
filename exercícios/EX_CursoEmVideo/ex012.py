p = float(input('qual o preço do produto?: '))
d = (p*5)/100
vt = p - d
print('o preço do deu produto era {} R$'.format(p))
print('voce recebeu 5% de desconto, portanto, o preço passa a ser {} R$'.format(vt))