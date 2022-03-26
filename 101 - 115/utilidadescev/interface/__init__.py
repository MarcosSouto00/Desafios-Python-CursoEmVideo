import colorama
colorama.init(autoreset=True)
def leiaInt(num):
  while True:
    try:
      n = int(input(num))
    
    except (ValueError, TypeError):
      print('\033[31mERRO! Digite uma opção valida')
      
    except KeyboardInterrupt:
      return 0
    
    else:
      return n

def linha(tam = 42):
  return '-' * tam

def cabecalho(txt):
  print(linha())
  print(txt.center(42))
  print(linha())
  
def menu(lista):
  cabecalho('MENU PRINCIPAL')
  cont = 1
  for item in lista:
    print(f'\033[33m{cont} - \033[34m{item}')
    cont += 1
  linha()
  opc = leiaInt('\033[32mSua Opção: ')
  return opc