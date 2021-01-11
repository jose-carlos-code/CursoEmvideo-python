import sys
import os
dic = {'1111':['Erick', 'Masc', 22],'2222':['Paulo','Masc',20],'3333':['Paula','Fem',21],'4444':['Erica','Fem',22]}
def inserir(chave):
    #chave=chave #str(input("Informe a matricula do aluno: "))
    nome=str(input("Informe o Nome do aluno:"))
    sexo=str(input("Informe o sexo do Aluno: "))
    idade=int(input("Informe a idade do Aluno: "))
    dic[chave]=[nome,sexo,idade]
def verifica(chave): #se retornar 1, significa que a chave existe, se retornar a chave significa que nao foi cadastrada.
    if chave not in dic:
        return chave
    else:
        return 1 #chave já cadastrada
def exclui(chave):
    dic.pop(chave)
def consultar(chave):
    item = dic[chave]
    matricula = chave
    nome = item[0]
    sexo = item[1]
    idade = item[2]
    return matricula,nome,sexo,idade
def alterar(chave):
    novalista=[]
    print("Re-insira todos os dados.")
    for e in dic[chave]:
        print(e)
        item=input("Altere para: ")
        novalista.append(item)
    dic[chave]=novalista
    print("Cadastro Alterado com sucesso!")
def option():
    print("##### CADASTRO DE ALUNOS #####\n")
    print("Informe a Opção\n ")
    print("1 - Inserir Aluno")
    print("2 - Excluir Aluno")
    print("3 - Alterar Aluno")
    print("4 - Consultar Aluno")
    print("5 - Exportar para JSON\n")
    print("0 - Sair")
    opcao=input(" ")
    return opcao
while True:
    opcao = option()
    while True:
        if opcao == "1":
            lost = input("Informe a matricula: ")
            if verifica(lost) == 1:
                print("Já existe um aluno com essa matricula.")
            else:
                inserir(verifica(lost))
            laco=input("Deseja continuar? s/n ? ")
            if laco == "n":
                os.system('clear')
                break
            else:
                os.system('clear')
        elif opcao == "2":
            lost = input("Informe uma matricula para excluir: ")
            if verifica(lost) == 1:
                exclui(lost)
                print("{} excluida com sucesso.".format(lost))
            else:
                print("Essa matricula ainda não foi casdastrada.")
            laco = input("Deseja continuar excluindo? s/n :")
            if laco == "n":
                os.system('clear')
                break
            else:
                os.system('clear')
        elif opcao == "3":
            lost = input("Informe a matricula para alterar: ")
            if verifica(lost) == 1:
                alterar(lost)
            else:
                print("{} não consta no sistema.".format(lost))
            laco = input("Deseja continuar alterando? s/n :")
            if laco == "n":
                os.system('clear')
                break
            else:
                os.system('clear')
        elif opcao == "4":
            lost = input("Informe a matricula: ")
            if verifica(lost) == 1:
                print("Matricula: {}".format(consultar(lost)[0]))
                print("Nome: {}".format(consultar(lost)[1]))
                print("Sexo: {}".format(consultar(lost)[2]))
                print("Idade: {}".format(consultar(lost)[3]))
            else:
                print("Essa Matricula ainda nao foi cadastrada.")
            laco = input("Deseja continuar consultando? s/n :")
            if laco == "n":
                os.system('clear')
                break
            else:
                os.system('clear')
        elif opcao == "5":
            print("Exportando para JSON...")
            print("Exportado com sucesso.")
        elif opcao == "0":
            sys.exit()
        else:
            print("Informe uma opção válida.")