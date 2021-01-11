a = float(input('informe o valor do primerito angulo: '))
b = float(input('informe o valor do segundo angulo: '))
c = float(input('informe o valor do terceiro angulo:'))
if a< b+c and b< a+c and c< b+a:
    print ('sim, com esses valores voce pode formar um triangulo')
else:
    print ('nao, voce nao pode formar um triangulo')
