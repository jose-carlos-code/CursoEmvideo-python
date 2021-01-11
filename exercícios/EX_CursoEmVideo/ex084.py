print('=-'*15, 'ANALISTA DE DADOS', '=-'*15)
grupo = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    if len(grupo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    grupo.append(dados[:])
    dados.clear()
    continuar = str(input('quer continuar?[S/N]: '))
    if continuar in 'Nn':
        break
print('=-'*30)
print(f'o total de pessoas cadastradas foi {len(grupo)}')
print(f'peso maior foi {maior}. o peso foi de', end=' ')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'o menor peso foi {menor} peso de', end=' ')
for c in grupo:
    if c[1] == menor:
        print(f'[{c[0]}]', end=' ')
print()