somaidade = 0
médiaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-----{}ªPESSOA-----'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]:')). strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehome, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'. format(totmulher20))