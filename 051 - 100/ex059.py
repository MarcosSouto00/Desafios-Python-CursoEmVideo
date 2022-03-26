while True:
  x = int(input('Digite um valor: '))
  y = int(input('Digite outro valor: '))
  lista = [x, y]
  print('Escolha Sua Ação')
  print('[ 1 ] Somar')
  print('[ 2 ] Multiplicar')
  print('[ 3 ] Maior')
  print('[ 4 ] Novos Números')
  print('[ 5 ] Fechar programa')
  escolha = int(input('Digite sua escolha: '))
  if escolha == 1:
      print(f'A soma dos dois valores é {x + y}')
  elif escolha == 2:
      print (f'O resultado da multiplicação dos dois valores é {x * y}')
  elif escolha == 3:
      print (f'O maior valor citado é {max(lista)}')
  elif escolha == 4:
    continue
  elif escolha == 5:
    break
  else:
    print ('Escolha inválida. Tente novamente')
    continue