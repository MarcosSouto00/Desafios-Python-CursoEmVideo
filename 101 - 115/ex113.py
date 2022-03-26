import colorama
colorama.init(autoreset=True)

def leiaInt(num):
  while num.isnumeric() == False:
    try:
      print('\033[31mERRO! Digite um numero inteiro válido')
      num = input('Digite um número inteiro: ')
    except KeyboardInterrupt:
      num = int(0)
      break
  if num.isnumeric() == True:
    return int(num)

def leiaFloat(num):
  n = num.replace('.', '')
  while n.isnumeric() == False:
    try:
      print('\033[31mERRO! Digite um numero inteiro válido')
      num = input('Digite um número real: ')
      n = num.replace('.', '')
    except KeyboardInterrupt:
      num = float(0)
      break
  if n.isnumeric() == True:
    return float(num)
        
        
x = leiaInt(input('Digite um número inteiro: '))
n = leiaFloat(input('Digite um número real: '))
print(f'Você digitou os número {x} e {n}')
