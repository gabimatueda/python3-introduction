import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O ângulo de {}, tem o seno de {:.2f}, cosseno de {:.2f}, e tangente de {:.2f}'. format(an, seno, cosseno, tangente))