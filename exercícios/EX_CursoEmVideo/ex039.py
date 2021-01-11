from datetime import date
atual = date.today().year
ano = int(input('olá, em que ano voce nasceu?: '))
idade = atual - ano
sexo = input('voce e homem ou mulher?: ')
if sexo == 'mulher':
    print('voce nao precisa se alistar no exército!, pois voce é mulher')
elif idade == 18:
    print('quem nasceu no ano {} tem {} ano(s) em 2019'.format(ano, idade))
    print('ja está na hora de se alistar')
elif idade < 18:
    print('quem nasceu no ano {} tem {} ano(s) em 2019'.format(ano, idade))
    print('ainda faltam {} ano(s) pra voce se alistar'.format(18 - idade, ))
    print('seu alistamento vai ser em {}'.format(atual + (18 - idade)))
else:
    print('quem nasceu no ano {} tem {} ano(s) em 2019'.format(ano, idade))
    print('voce deveria ter se alistado há {} ano(s)'.format(idade - 18))
    print('seu alistamento foi em {}'.format(atual - (idade - 18)))
