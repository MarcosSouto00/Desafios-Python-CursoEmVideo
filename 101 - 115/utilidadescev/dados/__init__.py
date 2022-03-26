import colorama

colorama.init(autoreset=True)
def leiaDinheiro(num):
  num = num.replace(',', '.')
  n = num.replace('.', '')
  
  while n.isnumeric() == False:
    print('\033[31mERRO! Digite um valor válido')
    num = input('Digite um valor: ')
    n = num.replace('.', '')
  return int(num)

