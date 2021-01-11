total =  mil = menor = 0
cont = 0
barato = ' '
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
    nome = str(input('nome do produto: '))
    preco = float(input('preço do produto: $'))
    cont +=1
    total+= preco
    if preco > 1000:
        mil+=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('quer continuar?: '))
    if continuar == 'n':
        break
print('-'*30, 'FIM DO PROGRAMA!',  '-'*30)
print(f'o total gasto na compra foi {total}$')
print(f'{mil} produtos custam mais de mil reais')
print(f'o produto mais barato foi o(a) {barato} que custa {menor}$')
