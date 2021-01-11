import datetime
atual = 2019
totm = 0
totn = 0
for c in range(1, 8):
    ano = int(input('qual o ano de nascimento da pessoa numero {}: '.format(c)))
    if atual - ano >= 18:
        totm += 1
    else:
        totn += 1
print('nessa lista existem {} pessoa maiores de idade e {} menores de idade'.format(totm, totn))
print('FIM')
