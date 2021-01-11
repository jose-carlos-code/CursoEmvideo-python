p = cont = soma = 0
while p != 999:
    p = int(input('digite um numero(999 para parar): '))
    if p != 999:
        soma += p
        cont += 1
print(f'o total de numeos digitadoa foi {cont}')
print(f'a soma de todos os numeros digitados é igual a {soma}')
print('FIM')
