n1 = int(input('me diga o primeiro numero: '))
n2 = int(input('me diga o segundo numero: '))
n3 = int(input('me diga o terceiro numero: '))
#verificando quem e maior
maior = n2
if n1 >2 and n1 >n2:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
#verificando quem e menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print ('o mair valor e {}'.format(maior))
print ('o menor valor {}'.format(menor))
