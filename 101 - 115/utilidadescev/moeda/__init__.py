def metade(num, f=False):
  num /= 2 
  if f == False:
    return num
  elif f == True:
    return f'R${num:.2f}'.replace('.', ',')

def dobro(num, f=False):
  num *= 2
  if f == False:
    return num
  elif f == True:
    return f'R${num:.2f}'.replace('.', ',')
  
def aumentar(num, n, f=False):
  num *= (100+n)/100
  
  if f == False:
    return num
  
  elif f == True:
    return f'R${num:.2f}'.replace('.', ',')

def diminuir(num, n, f=False):
  num *= (100-n)/100
  if f == False:
    return num
  elif f == True:
    return f'R${num:.2f}'.replace('.', ',')

def moeda(num):
  return f'R${num:.2f}'.replace('.', ',')

def resumo(n, n2, n3):
  print('----------------------------')
  print('     RESUMO DOS VALORES     ')
  print('----------------------------')
  print(f'Preço analisado: \t{moeda(n)}')
  print(f'Dobro do Preço:  \t{dobro(n, True)}')
  print(f'Metade do Preço: \t{metade(n, True)}')
  print(f'{n2}% de Aumento: \t{aumentar(n, n2, True)}')
  print(f'{n3}% de Desconto: \t{diminuir(n, n3, True)}')
  print('----------------------------')