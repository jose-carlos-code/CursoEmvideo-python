contador = maior18 = 0
h = m = 0
while True:
    print('-'*30)
    print('CADASTRO DE PESSOAS!')
    print('-'*30)
    contador += 1
    idade = int(input(f'qual a idade da pessoa {contador}? :'))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input(f'qual o sexo da pessoa(m/f) {contador}?: ')).upper()
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('quer continuar?(s/n): ')).upper()
    if idade > 18:
        maior18+=1
    if sexo == 'm':
        h+=1
    if sexo == 'f' and idade < 20:
        m+=1
    if continuar == 'n':
         break
print('NESSA LISTA: ')
print('-'*30)
print(f'{maior18} pessoa(s) possuem mais de 18 anos')
print(f'{h} homen(s) foram cadastrados')
print(f'{m} meulher(s) possuem menos de vinte anos de idade')
print('-'*30)