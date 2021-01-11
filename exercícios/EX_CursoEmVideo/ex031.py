d = float(input('me diga a distancia da sua viagem: '))
p1 = 0.50*d
p2 = 0.45*d
if d<=200:
    print ('o preco dessa viagem vai ser R${}'.format(p1))
else:
    print ('o preco da sua viagem vai ser R${}'.format(p2))
