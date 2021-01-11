d = float(input('quanto de dinheiro voce tem na carteira?: '))
c = d/3.27
if c<1:
    print (' voce tem apenas {}$,xiii, voce nao pode comprar nem um dolar'.format(d))
    print ('seu valor convertido em dolares ficar em apenas {}US$'.format(c))
else:
    print (' voce tem {}$, voce pode comprar {}US$'.format(d, c))