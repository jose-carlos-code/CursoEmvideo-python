c = 's'
contador = soma = maior = menor = 0
while c != 'n':
    n = int(input('digite o numero que voce deseja aqui: '))
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('quer continuar[s/n]?: '))
print(f'voce digitou {contador} valores e a media entre eles é {soma/contador :.2f}')
print(f'o maior numero digitado foi {maior} e o menor foi {menor}')
