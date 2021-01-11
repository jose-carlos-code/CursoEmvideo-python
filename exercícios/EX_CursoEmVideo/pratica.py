#josé carlos
#exercício 7
#controle da utilização das salas de um cinema

salas = [1, 2, 3, 4, 5]
lugares = [10, 2, 1, 3, 0]
while True:
  opcao = int(input('digite o númer da sala(0 para sair): '))
  quant = int(input('quantos lugares você deseja?: '))
  if quant <= lugares[opcao-1]:
    lugares[opcao-1] -= quant
  else:
    print('que pena. nãp temos lugares suficientes nessa sala')
    print(f'restaram apenas {lugares[opcao-1]} nesta sala')
