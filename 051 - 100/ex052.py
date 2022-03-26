num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
  if (num % c) == 0:
    cont += 1
    print('\033[32m', end=' ')
  else:
    print('\033[31', end=' ')
  print(f'{c}', end=' ') 
if cont == 2:
  print(f'\nEle foi divisivel por {cont} números. Ele é primo')
else:
 print(f'Ele foi divisivel por {cont} números. Ele não é primo')