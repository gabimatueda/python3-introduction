from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento:'))
idade = atual - nasc
alistamento = 18 - idade
ano = alistamento + atual
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade <18:
     print('Ainda faltam {} anos para o alistamento'. format(alistamento))
     print('Seu alistamento será em {}'. format(ano))
elif idade ==18:
    print('Você já pode se alistar')
    print('{} é seu ano de alistamento'.format(ano))
elif idade >18:
    print('Seu alistamento foi em {}'.format(ano))
