def notas(*num, sit=False):
    """
    funcão para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre situação da turma
    """

    dados = dict()
    soma = 0
    quant = 0#armazena quantos numero tem em NUM
    for n in num:
        soma += n
        quant +=1
    m = soma/quant
    dados['total'] = quant
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = m
    if sit == True:
        if m < 6:
            dados['situação'] = 'ruim'
        elif m < 7:
            dados['situação'] = 'razoavel'
        else:
            dados['situação'] = 'boa'
    return dados


resp = notas(4.5, 10, 6.5,sit=True)
print(resp)