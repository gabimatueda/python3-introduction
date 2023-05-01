r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = r / 5.22
e = r / 5.56
i = r / 0.039
print('Com R${:.2f} você pode comprar US${:.2f}, {:.2f} euros, {:.2f} ienes.'. format(r, d, e, i))

