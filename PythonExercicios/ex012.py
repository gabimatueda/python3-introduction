preço = float(input('Qual é o preço do produto?R$'))
desconto = preço - (preço*20/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 20% vai custar R${:.2f}'. format(preço, desconto))