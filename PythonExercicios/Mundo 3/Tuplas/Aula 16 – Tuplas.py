lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print('=' * 30)
for cont in range(0, len(lanche)):
    print(cont)
print('=' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print('=' * 30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
print('Comi pra caramba')
print('=' * 30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')
print('Comi pra caramba')
print('=' * 30)
print(sorted(lanche)) #sorted coloca em ordem
print('=' * 30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))