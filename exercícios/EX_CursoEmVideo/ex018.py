import math
numero = float(input('digite o valor de um ângulo: '))
s = math.sin(math.radians(numero))
c = math.cos(math.radians(numero))
t = math.tan(math.radians(numero))
print('o seno de {} é {:.2f}'.format(numero,s))
print('o cosseno de {} é {:.2f}'.format(numero,c))
print('a tangente de {} é {:.2f}'.format(numero,t))
