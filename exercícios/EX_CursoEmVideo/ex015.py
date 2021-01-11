k = float(input('você rodou quantos kilometros com esse carro?: '))
d = int(input('quantos dias voce passou com ele?: '))
c1 = 60 * d
c2 = 0.15 * k
cf = c1 + c2
print('voce vai pagar {} R$ '.format(cf))
