casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {}, a prestação será de {:.2f}'.format(casa, anos, prestação))
print('COMPARANDO tem que pagar R${:.2f} e o mínimo é de R${}'.format(prestação,mínimo))
if prestação <=mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')