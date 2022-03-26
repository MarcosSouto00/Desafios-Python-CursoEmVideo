import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print (f'o angulo {angulo} tem o SENO de {seno:.2f} \no COSSENO de {cosseno:.2f} \ne a TANGENTE de {tangente:.2f}')