lista= []
while True:
    lista.append(int(input('Digite um valor: ')))
    r= str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 20)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')