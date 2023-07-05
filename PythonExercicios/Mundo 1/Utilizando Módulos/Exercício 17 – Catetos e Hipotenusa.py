co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'. format(hip))
import math #Outro jeito de fazer
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hip = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'. format(hip))
from math import hypot #Outro jeito de fazer
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))