sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = str(input('qual o sexo da pessoa? M/F?: ')).lower()
    if sexo != 'm' and sexo != 'f':
        print('sexo inexistente, SEU PORRA!')
        print('por favor, digite novamento o sexo')
print('FIM')
