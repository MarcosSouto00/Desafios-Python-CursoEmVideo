from random import randint

tent = 1
x = randint(0, 10)
n = int(input('Digite um numero de 1 a 10: '))
if n == x:
    print ('Você Ganhou De PRIMEIRA!!')
elif n != x:
  while n != x:
    if n > x:
      n = int(input('Menos, Tente Novamente: '))
      tent += 1
    if n < x:
      n = int(input('Mais, Tente Novamente: '))
      tent += 1
  if n == x:
    print (f'Você ganhou com {tent} tentativas')
