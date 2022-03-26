vel = int(input('Digite a velocidade do carro com apenas números! '))
dif = vel - 80
val = dif * 7
if vel < 81:
  print ('Muito bem, você esta na velocidade correta')
else:
  print (f'Você está {dif}KM/h acima do limite. Sua multa é de R${val}')