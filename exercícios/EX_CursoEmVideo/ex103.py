def ficha(nome='<desconhecido>', gols=0):
    print(f'o jogador {nome} fez {gols} gol(s)')


# --> PROGRAMA PRINCIPAL <--
nome = str(input('nome do jogador: '))
ngols = str(input('numero de gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if nome.strip() == '':
    ficha(gols=ngols)
else:
    ficha(nome, ngols)