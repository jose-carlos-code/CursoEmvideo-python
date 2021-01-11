from datetime import date
ano = int(input('que ano voce quer analisar? digite zero para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('{} e um ano bissexto'.format(ano))
else:
    print ('{} e um ano comum'.format(ano))