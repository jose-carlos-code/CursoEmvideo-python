v = int(input('qual a velocidade do seu carro?: '))
b = v - 80
m = 7*b
if v>80:
    print ('voce ultrapassou o limite de velocidade!')
    print ('voce foi multado!')
    print ('a multa vai custar {}'.format(m))
else:
    print ('meus parabens, voce esta na velocidade adequada!')


