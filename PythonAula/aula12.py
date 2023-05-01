nome = str(input('Qual é seu nome? '))
if nome == 'Gabriela':
    print('Que nome espetacular')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é tão comum')
elif nome in 'Princesa Ivone Jorge':
    print('Que belo nome')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'. format(nome))