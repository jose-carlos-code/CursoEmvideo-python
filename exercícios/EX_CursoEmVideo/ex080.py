num = list()
for c in range(0, 5):
    valor = (int(input('digite um valor: ')))
    if c == 0 or valor > num[-1]:
        num.append(valor)
        print(f'o valor foi adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if valor <=num[pos]:
                num.insert(pos, valor)
                print(f'o valor foi adicionado na posição {pos}')
                break
            pos +=1
print('-='*30)
print(f'em ordem, os numeros adicionados foram: {num}')
print('-='*30)