def fatorial(n, show=False):
  """
  Fatora um número
  n = numero a ser fatorado
  show(opc) = deicidi se mostra ou nao o calculo
  return = retorna o numero fatorado
  """
  
  contador = 1
  
  while n > 0:
    if show == True:
      if n > 1:
        print(f'{n} x ', end='')
      if n == 1:
        print(f'{n} = ', end='')
    contador *= n
    n = n - 1
  
  return contador
  

print(fatorial(5, True))