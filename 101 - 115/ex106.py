import colorama

colorama.init()

def text(txt):
  print('\033[30;44m~' * (len(txt)+35))
  print(f'  Accessando o Manual do Comando {txt}  ')
  print('~' * (len(txt)+35))
  
while True:
  print('\033[30;42m~~~~~~~~~~')
  print('  PyHelp  ')
  print('~~~~~~~~~~\033[m')

  func = input('Função ou Biblioteca: ')

  if func.upper() == 'FIM':
    break
  
  text(func)
  
  help(func)