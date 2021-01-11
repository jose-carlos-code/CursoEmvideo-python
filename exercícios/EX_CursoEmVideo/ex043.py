peso = float(input('qual o seu peso?: '))
altura = float(input('qual a sua altura?: '))
imc = peso/ (altura**2)
print('o IMC da pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc <25:
    print('peso ideal')
elif imc >=25 and imc < 30:
    print('sobrepeso')
elif imc >=30 and imc <40:
    print('obesidade')
elif imc >40:
    print('obesidade mórbida')
