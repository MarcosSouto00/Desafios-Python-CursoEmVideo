fr = input('Digite um nome/frase: ').upper().replace(' ', '')
print (f'{fr} ao contrario é {fr[::-1]}')
if fr == fr[::-1]:
  print ('Isso é um palíndromo!!')
else:
  print ('Não é um palíndromo')