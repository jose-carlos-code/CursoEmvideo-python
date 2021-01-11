dicio = dict()
ngols = list()
totgol = gol = 0
dicio['nome'] = str(input('nome do jogador: '))
partidas = int(input('quantas partidas ele jogou?: '))
for contador in range(1, partidas+1):
    gol = int(input(f'quantos gols ele fez na partida {contador -1} ?: '))
    totgol += gol
    ngols.append(gol)
dicio['gols'] = ngols[:]
dicio['total'] = totgol
print('=-'*30)
print(dicio)
print('=-'*30)
for i, v in dicio.items():
    print(f'o campo {i} tem valor {v}')
print('=-'*30)
print(f'o jogador{dicio["nome"]} jogou {len(dicio["gols"])}')
for c in range(0, len(dicio['gols'])):
    print(f'=> Na partida {c}, fez {ngols[c]}')
