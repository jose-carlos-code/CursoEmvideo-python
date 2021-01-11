s = float(input('me diga o seu salario: '))
a = s*15/100
b = s *10/100
if s <= 1250:
    print ('o seu salario tera um aumento de 15%')
    print ('seu salario aumentou de {} para {}'.format(s, a+s))
else:
    print('o seu salario vao ter um aumento de 10%')
    print ('o seu salario aumentou de {} para {}'.format(s, b+s))


