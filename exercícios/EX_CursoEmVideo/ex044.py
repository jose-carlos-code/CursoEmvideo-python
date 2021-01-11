print('{:=^40}'.format(' LOJAS CAMPOS '))
preço = float(input('qual o preço do produto?: '))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2X no cartão
[4] 3X ou mais no cartão''')
opcçao = int(input('qual a opção?: '))
if opcçao == 1:
    total = preço - (preço*10/100)
elif opcçao == 2:
    total = preço - (preço*5/100)
elif opcçao == 3:
    total = preço
    parcela = total/2
    print('sua compra  sera parcelada em 2X de R${:.2f} SEM JUROS'.format(parcela))
elif opcçao == 4:
    total = preço + (preço*20/100)
    totparc = int(input('quantas parcelas?: '))
    parcela = total/totparc
    print('sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('opcção inválida de pagamento. tente novamente!')
print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))