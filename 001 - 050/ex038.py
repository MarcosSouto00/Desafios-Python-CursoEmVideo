x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
if x > y:
  print (f'{x} é maior que {y}')
elif y > x:
  print (f'{y} é maior que {x}')
else:
  print ('Os dois valores são iguais')