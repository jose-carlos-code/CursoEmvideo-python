from datetime import  datetime
aposent = dict()
aposent['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
idade = datetime.now().year - nasc
aposent['idade'] = idade
aposent['ctps'] = int(input('numero da carteira de trabalho(0 não tem): '))
if aposent['ctps'] == 0:
    print('=-' * 30)
    for i, v in aposent.items():
        print(f'{i} tem valor {v}')
else:
    print('=-' * 30)
    aposent['contratação'] = int(input('ano de contratação: '))
    aposent['salário'] = float(input('salário: '))
    aposent['aposentadoria'] = (aposent['contratação'] - nasc) + 35
    for i, v in aposent.items():
        print(f'{i} tem valor {v}')