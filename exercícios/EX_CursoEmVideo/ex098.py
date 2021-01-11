from time import sleep
def contador(i, f, p):
    if i < f:
        if p == 0:
            p = 1
        for c in range(i, f+1, abs(p)):
            sleep(0.2)
            print(c, end=' ')
        print()
    elif i > f:
        if p == 0:
            p = -1
        elif p > 0:
            p = p - (p*2)
        for c in range(i, f-1, p):
            sleep(0.3)
            print(c, end=' ')
        print()


contador(1, 10, 1)
contador(10, 0, -2)
incio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(incio, fim, passo)
print('FIM!')