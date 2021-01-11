temp = dict() #lista temporária, para guardar os dados
dados = {} #dicionário para guardar os dados
lista = list() #lista para guardar os dicionários com os dados
contador =  0
media = [] #lista que guara as idades
mulher = list() # lista que guarda todas as mulheres
pessoas = 0 # variáveil para as pessoas com idade acima da media
while True:
    temp['nome'] = str(input('nome:')).lower()
    contador += 1
    temp['idade'] = int(input('idade: '))
    media.append(temp['idade'])
    while True:
        temp['sexo'] = str(input('sexo[m/f]: ')).lower()[0]
        if temp['sexo'] in 'mf':
            break
        print('ERRO! utilize apenas: M ou N)')
    if temp['sexo'] == 'f':
        mulher.append(temp['nome'])
    dados = temp.copy()
    temp.clear()
    lista.append(dados.copy())
    dados.clear()
    while True:
        continuar = str(input('quer continuar?[s/n] '))
        if continuar in 'sn':
            break
        print('ERRO! utilize apenas: S ou N)')
    if continuar == 'n':
         break
calc = sum(media)/len(media)
print('-='*15, 'DADOS DA LISTA', '-='*15)
print(f'o total de pessoas cadastradas foi {contador}')
print(f'a media da idade do grupo é {calc:.1f}')
print(f'as mulheres cadastradas foram: {mulher}')
print(f'pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] >= calc:
        print(' ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(lista)
print('ENCERRADO.')