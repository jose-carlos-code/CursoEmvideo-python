def voto(nasc):
    idade = 2020 - nasc
    if 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: voto opcional'.upper()
    elif idade < 16:
        return f'com {idade} anos: não vota'
    else:
        return f'com {idade} anos: voto obrigatótio'.upper()


idade = int(input('em que ano você nasceu?: '))
print(voto(idade))
