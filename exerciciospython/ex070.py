total = maisdemil = menor = cont = 0
barato = ' '
while True:
    print('-----LOJA DO SUPER BARATÃO-----')
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-----FIM DO PROGRAMA-----')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')