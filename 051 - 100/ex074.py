from random import randint

x = randint(0, 9)
y = randint(0, 9)
z = randint(0, 9)
xy = randint(0, 9)
xz = randint(0, 9)
n = x, y, z, xy, xz
print(f'Os valores sorteados foram {n}\no maior valor é {max(n)}\no menor valor sorteado é {min(n)}')
