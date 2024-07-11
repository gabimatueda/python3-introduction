peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é a sua altura? (m)'))
IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'. format(IMC))
if IMC < 18.5:
    print('Você está na faixa de ABAIXO DO PESO')
elif 18.5 < IMC < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 < IMC < 30:
    print('Você está na faixa de SOBREPESO')
elif 30 < IMC < 40:
    print('Você está na faixa de OBESIDADE')
elif IMC >= 40:
    print('Você está na faixa de OBESIDADE MÓRBIDA')