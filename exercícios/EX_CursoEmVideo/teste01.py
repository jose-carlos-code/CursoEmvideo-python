def linha():
    print('-='*15)


cpf = dict()
pessoas = list()
num = ''
while num != 5:
    linha()
    print("""
    \033[mDIGITE [1] PARA ADICIONAR UM CPF
    DIGITE [2] PARA ALTERAR UM CPF
    DIGITE [3] PARA EXCLUIR UM CPF
    DIGITE [4] PARA VISUALIZAR TODOS OS CPFS CADASTRADOS
    DIGITE [5] PARA SAIR""")
    while True:
        linha()
        num = int(input('digite aqui: '))
        linha()
        if num < 1 or num > 5:
            print('ERRO! digite um número válido')
        else:
            break
    while True:
        if num == 1:
            temp = str(input('\033[1;33madicione um cpf: '))
            nome = str(input('digite o nome da pessoa: '))
            if temp not in pessoas:
                cpf[temp] = nome
                pessoas.append(cpf[temp])
            else:
                print('\033[35mCPF JÁ CADASTRADO!')
        break
    if num == 4:
        print(pessoas)