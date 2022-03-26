from random import randint

numeros = []

def sorteio(lst):
  print('Números sorteados:', end=' ')
  
  for c in range(0, 5):
    x = randint(0, 10)
    print(x, end=' ')
    lst.append(x)

  print()
  
def somapar(numeros):
  sp = 0
  
  for c in numeros:
    if c % 2 == 0:
      sp += c
  
  print(f'Somando os valores pares de {numeros}, temos {sp}')
  
sorteio(numeros)
somapar(numeros)