import math
co = float(input('qual o valor do cateto oposto?: '))
ca = float(input('qual o valor do cateto adjacente?: '))
hip = math.hypot(co, ca)
print('o valor da hipotenusa é {:.2f}'.format(hip))
