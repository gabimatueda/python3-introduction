import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {}'. format(num, math.ceil(raiz)))
from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é {}'. format(num, floor(raiz)))