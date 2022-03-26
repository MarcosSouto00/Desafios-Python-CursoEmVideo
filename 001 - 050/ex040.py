n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2
if media <= 5.0:
  print ('Reprovado')
elif media <= 6.9:
  print ('Recuperação')
elif media >= 7.0:
  print ('Aprovado')