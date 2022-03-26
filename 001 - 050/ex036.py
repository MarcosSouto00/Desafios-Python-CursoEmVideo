valorcasa = float(input('Digite o valor da casa '))
salario = float(input('Digite seu salario '))
tempo = int(input('Quantos anos você vai passar pagar essa casa? '))
meses = tempo * 12
parcela = valorcasa / meses
saldividido = salario * 0.30
if parcela <= saldividido:
  print (f'Você terá que pagar {parcela} por {meses} meses')
else:
  print ('As parcelas são muito altas')