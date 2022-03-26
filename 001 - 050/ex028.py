from random import randint
x = randint(0, 5)
n = int(input('Digite um numero de 1 a 5: '))
if n == x:
  print ('Você Ganhou!!')
else:
  print(f'Você perdeu!! O número era {x}')