n = int(input('Digite a distancia da viagem: '))
vc = n * 0.50
vl = n * 0.45
if n <= 200:
  print (f'O valor será {vc}')
else:
  print (f'O valor será {vl}')