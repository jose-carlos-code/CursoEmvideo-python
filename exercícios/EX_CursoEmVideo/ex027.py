nome = str(input('qual o seu nome completo?: ')).strip()
d = nome.split()
print('o seu primeiro nome é {}'.format(d[0]))
print('o seu ultimo nome é {}'.format(d[len(d)-1]))

