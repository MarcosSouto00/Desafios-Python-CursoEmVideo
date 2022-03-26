pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
c = 0
while c < 10:
  print(pt, end=' → ')
  pt += rz
  c += 1
print('ACABOU')
