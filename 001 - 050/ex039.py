ano = int(input('Digite seu ano de nascimento: '))
idade =  2022 - ano
if idade <= 17:
  print (f'Ainda faltam {18 - idade} anos para você se alistar')
elif idade == 18:
  print ('Você ja esta na idade de se alistar. Boa Sorte!')
elif idade > 18:
  print (f'Você ja passou {idade-18} anos da idade de se alistar')