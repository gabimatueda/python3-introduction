teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('-=' * 20)
pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas[2][1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')
print('-=' * 20)
people = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    people.append(dado[:])
    dado.clear()
for p in people:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')