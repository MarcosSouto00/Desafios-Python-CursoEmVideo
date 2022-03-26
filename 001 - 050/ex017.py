from math import hypot as hipotenusa
co = float(input('Comprimento do cateto oposto '))
ca = float(input('Comprimento do cateto adjacente '))
hi = hipotenusa(co, ca)
print (f'A hipotenusa vai medir {hi:.2f}')