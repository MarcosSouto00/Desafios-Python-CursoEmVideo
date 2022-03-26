from time import sleep


print('-=-=-=-=-=-=-=-=-=-=-=-=-')

def cont(x, y, z):
  
  if z == 0:
    z = 1
    
  if z < 0:
    print(f'Contagem de {x} até {y+1} de {z * -1} em {z * -1}')
  
  else:
    print(f'Contagem de {x} até {y-1} de {z} em {z}')
    
  if y < x and z > 0:
    z = z * -1

 
  for c in range(x, y, z):
    print(c, end=' ')
  
  print()
  
  print('-=-=-=-=-=-=-=-=-=-=-=-=-')


cont(1, 11, 1)

cont(10, -1, -2)

x = int(input('Inicio: '))
y = int(input('Fim: '))
z = int(input('Passo: '))

cont(x, y, z)
