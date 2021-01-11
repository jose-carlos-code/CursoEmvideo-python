n1 = float(input('qual a primeira nota do aluno?: '))
n2 = float(input('qual a segunda nota do aluno?: '))
media = (n1 + n2)/2
if media < 5.0:
    print('a media do aluno foi {}, aluno REPROVADO!'.format(media))
elif media >=5 and media <=6.9:
    print('a media do aluno foi {}, aluno em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('a meida do aluno foi {}, aluno APROVADO!'.format(media))
