ano = int(input('Digite o ano de nascimento do nadador: '))
idade = 2022 - ano
if idade <= 9:
  print ('Ele é Mirim')
elif 9 < idade <= 14:
  print ('Ele é Infantil')
elif 14 < idade <= 19:
  print ('Ele é Junior')
elif 19 < idade <= 20:
  print ('Ele é Sênior')
elif 20 < idade:
  print ('Ele é Master')