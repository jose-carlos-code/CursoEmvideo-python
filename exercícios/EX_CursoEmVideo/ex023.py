num = int(input('me diga um numero entre 0 e 9999: '))
u = num // 1 %10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('você digitou o número {} '.format(num))
print('ele tem:  ')
print('----------------------------------------------')
print('unidade: {}'.format(u))
print('dezena : {}'.format(d))
print('centena: {}'.format(c))
print('milhar:  {}'.format(m))