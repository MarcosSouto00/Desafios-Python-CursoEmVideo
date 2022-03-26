n = input('Digite uma operação: ')
lista = []
for c in n:
  if c == '(':
    lista.append('(')
  elif c == ')':
    if len(lista) > 0:
      lista.pop()
    else:
      lista.append(')')
      break
if len(lista) == 0:
  print('Essa expressão é valida')
else:
  print('Essa esxpressão é invalida')