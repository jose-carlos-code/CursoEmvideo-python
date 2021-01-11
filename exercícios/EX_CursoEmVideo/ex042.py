a = float(input('informe o valor do primerito angulo: '))
b = float(input('informe o valor do segundo angulo: '))
c = float(input('informe o valor do terceiro angulo:'))
if a< b+c and b< a+c and c< b+a:
    print ('sim, com esses valores voce pode formar um triangulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a!= b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print ('nao, voce nao pode formar um triangulo')
