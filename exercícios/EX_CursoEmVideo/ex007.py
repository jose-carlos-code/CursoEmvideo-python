n1 = float(input('qual a primeira nota do aluno?: '))
n2 = float(input('qual a segunda nota do aluno?: '))
n3 = float(input('qual a terceira nota do aluno?: '))
n4 = float(input('qual a quarta nota do aluno?: '))
m = n1 + n2 + n3 + n4
if m >= 28:
    print ('parabens, sua media foi {}, voce esta aprovado!'.format(m))
else:
    print ('sua  nota foi {}, voce esta reprovado'.format(m))
    print ('estude mais da proxima vez')