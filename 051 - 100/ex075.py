x = int(input('Digite um valor'))
y = int(input('Digite um valor'))
z = int(input('Digite um valor'))
xy = int(input('Digite um valor'))
xz = int(input('Digite um valor'))
n = x, y, z, xy, xz
par = 0
for num in n:
  if num % 2 == 0:
    par += 1
print(f'''Você digitou os valores {n}
O valor 9 apareceu {n.count(9)+1}° posiçâo
O valor 3 apareceu pela primeira vez na {n.index(3)}
Os valores pares digitados foram {par}
''')