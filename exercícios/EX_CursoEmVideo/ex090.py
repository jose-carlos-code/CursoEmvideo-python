dados = dict()
dados['nome'] = str(input('nome: '))
dados['media'] = float(input('media: '))
print('=-'*30)
print(f'nome: {dados["nome"]}')
print(f'media: {dados["media"]}', end='')
print()
if dados['media'] >= 7:
    print(f'sutuação: aprovado')
else:
    print(f'situação: reprovado')