peso = float(input('Digite seu peso(em KG e apenas números e pontos Ex: 45.5): '))
altura = float(input('Digite seu tamanho(em metros e apenas númerose pontos Ex: 1.60): '))
imc = peso / (altura ** 2)
print (f'Seu IMC é {imc:.2f}')
if imc < 18.5:
  print ('Você está abaixo do peso ideal')
if 18.5 <= imc < 25:
  print ('Você está no peso ideal')
if 25 <= imc < 30:
  print ('Você está com sobrepeso')
if 30 <= imc < 40:
  print ('Você tem obesidade')
if 40 <= imc:
  print ('Você tem obesidade mórbida')