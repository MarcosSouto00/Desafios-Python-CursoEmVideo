pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
for c in range (pt, (pt + (10-1) * rz)+rz, rz):
  print(f'{c}', end=" → ")
print('ACABOU')