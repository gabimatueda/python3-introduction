cidade = str(input('Em que cidade você nasceu?')).title().split()
print('Santo' in cidade[0])
cid = str(input('Em que cidade você nasceu? ')).strip() #Outro jeito de fazer
print(cid[:5].upper() == 'SANTO')