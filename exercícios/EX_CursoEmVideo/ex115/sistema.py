from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair Do Sistema'])
    if resposta == 1:
        #opção  de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaInt('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('saindo do sistema... até logo')
        break
    else:
        print('\033[31mERRO! digite uma opção válida\033[m')
    sleep(0.8)