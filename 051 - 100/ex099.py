from time import sleep

print('-=-=-=-=-=-=-=-=-=-=-')

def maior(*num):
  cont = maiorn = 0
  
  for c in num:  
    print(c, end=' ')
    sleep(0.5)
    
    cont += 1
    
    if c > maiorn:
      maiorn = c
  
  print(f'foram informados {cont} valores ao todo')
  print(f'O maior valor informado foi {maiorn}')
  print('-=-=-=-=-=-=-=-=-=-=-')
  

maior(1, 5, 6, 9, 10, 89, 4)
maior()
maior(5, 7, 8)
maior(1)