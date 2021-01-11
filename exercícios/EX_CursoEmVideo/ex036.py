nome = str(input('qual o seu nome?: '))
salario = float(input('qual o seu salário?: '))
v = float(input('bom dia, qual o valor da casa?: '))
ano = float(input('em quantos anos voce quer pagar esta casa?: '))
calculo = v / (ano * 12)
mensal = calculo
if (mensal * 100) / salario >= 30:
    print('------------------------------------------------------------------')
    print('sinto muito {}, mas voce nao podera comprar a casa...'.format(nome))
    print('pois, o valor a pagar ( {:.1f}R$ ) excedeu 30% do seu salario.'.format(mensal))
    print('------------------------------------------------------------------')
else:
    print('------------------------------------------------------------------')
    print('meus parabens {}, seu empréstimo foi aceito!'.format(nome))
    print('voce deverá pagar {:.2f} R$ por mês durante {} anos'.format(mensal, ano))
    print('------------------------------------------------------------------')