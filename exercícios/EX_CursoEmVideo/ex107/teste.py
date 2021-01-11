from ex107 import moeda
p = float(input('digite o preço: R$'))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'diminuindo 13%, temos {moeda.diminuir(p, 13)}')
