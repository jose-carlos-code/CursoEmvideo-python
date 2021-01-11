from time import sleep
from datetime import date
salario = 0
ano_atual = date.today().year
media = 0 #variavel para calcular a media
resp = ''
contador = 0#contador para auxiliar no calculo da média
maior = 0 #variavel que guarda o maior salário
maiorList = list()#lista que guarda nome e o setor da pessoa com o maior salario
while True:
  nome = str(input('digite o nome do funcionário: '))
  while True:
    salario = float(input(f'informe o salário do funcionário {nome}: '))
    if salario >= 1045:
      media += salario
      contador +=1
      break
    print('\033[33merro! digite um salário válido\033[m')
  while True:
    nasc = int(input(f'informe o ano de nascimento do funcionário {nome}: '))
    idade = ano_atual - nasc
    if idade >= 16:
      break
    print('\033[33merro! idade inválida\033[m')
  setor = int(input(f'digie o setor do funcionário {nome}: '))
  if contador == 1:
      maior = salario
  if salario >= maior:
    maior = salario
    maiorList.clear()
    maiorList.append(nome)
    maiorList.append(setor)
    maiorList.append(maior)
  while True:
    resp = str(input('deseja adicionar outro funcionário?[s/n]: ')).lower()
    if resp in 'sn':
      break
    print('\033[33merro! digite apenas S ou N\033[m')
  if resp == 'n':
    print('FINALIZANDO...')
    sleep(1)
    break
print("""
        ----------------------
        DADOS DOS FUNCIONÁRIOS
        ----------------------
""")
print(f'a pessoa com o maior salário é {maiorList[0]}, do setor {maiorList[1]}, que recebe {maiorList[2]}')
print(f'a média salarial dos funcionários é R${media/contador:.2f}')