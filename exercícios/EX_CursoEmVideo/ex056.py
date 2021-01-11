somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('------- {}° pessoa --------'.format(c))
    sexo = str(input('qual o sexo da pessoa M/F?: ')).lower()
    nome = str(input('qual o nome dele(a)?: ')).lower()
    idade = int(input('qual a idade dessa pessoa?: '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('a media de idade desse grupe é {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}'.format(maiorhomem, nomevelho))
print('ao todo sao {} mulheres com menos de vinte anos'.format(totmulher20))