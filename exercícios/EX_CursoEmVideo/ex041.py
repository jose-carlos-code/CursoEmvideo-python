from datetime import date
atual = date.today().year
ano = int(input('qual o ano de nascimento do atleta?: '))
idade = atual - ano
if idade <= 9:
    print('quem nasceu em {} tem {} anos'.format(ano, idade))
    print('é um atleta MIRIM"')
elif 14 >= idade > 9:
    print('quem nasceu em {} tem {} anos'.format(ano, idade))
    print('é um atleta INFANTIL!')
elif idade > 14 and idade <=19:
    print('quem nasceu em {} tem {} anos'.format(ano, idade))
    print('o atleta é JUNIOR!')
elif idade == 20:
    print('quem nasceu em {} tem {} anos'.format(ano, idade))
    print('o atleta é SÊNIOR!')
else:
    print('quem nasceu em {} tem {} anos'.format(ano, idade))
    print('o atleta é MASTER!')