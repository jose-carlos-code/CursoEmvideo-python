import os
e=0
dic = {'123456':['erick', 'masc', 22]}
def inserir(chave):
    chave = chave #str(input("Informe a matricula do aluno: "))
    nome=str(input("Informe o Nome do aluno:"))
    sexo=str(input("Informe o sexo do Aluno: "))
    idade=int(input("Informe a idade do Aluno: "))
    dic[chave]=[nome,sexo,idade]
def verifica(chave):
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

    
while e != 4:
    lost = input("Informe a matricula: ")
    if verifica(lost) == 1:
        print("Já existe um aluno com essa matricula.")
    else:
        inserir(verifica(lost))
    e += 1
    print(dic)
while e != 3:
    lost = input("Informe uma matricula para excluir: ")
    if verifica(lost) == 1:
        exclui(lost)
        print("{} excluida com sucesso.".format(lost))
        print(dic)
    else:
        print("Essa matricula ainda não foi casdastrada.")
        print(dic)
while e != 4:
    lost=input("Informe a matricula: ")
    if verifica(lost) == 1:
        print("Matricula: {}".format(consultar(lost)[0]))
        print("Nome: {}".format(consultar(lost)[1]))
        print("Sexo: {}".format(consultar(lost)[2]))
        print("Idade: {}".format(consultar(lost)[3]))
    else:
        print("Essa Matricula ainda nao foi cadastrada.")