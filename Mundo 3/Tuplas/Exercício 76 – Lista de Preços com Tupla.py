listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.90,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range (0, len(listagem)): #pos é posição
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')  #se for par ele mostra o nome do produto
    else:
        print(f'R${listagem[pos]:>7.2f}')  #se for ímpar ele mostra o preço
print('-' * 40)