from random import randint

cont = 0
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
p = True
while p == True:
  x = randint(0, 10)
  y = int(input('Digite um valor de 0 - 10: '))
  z = input('Escolha Par ou Impar [P/I]: ').upper()
  soma = x + y
  if soma % 2 == 0:
    print(f'------------------------------')
    print(f'Você jogou {y} e o computador {x}. Total de {soma} DEU PAR')
    print(f'------------------------------')
    if z == 'P':
      print('Você VENCEU')
      cont += 1
      print('Vamos jogar novamente...')
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif z == 'I':
      print('Você PERDEU')
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
      p = False
if soma % 2 == 1:
    print(f'------------------------------')
    print(f'Você jogou {y} e o computador {x}. Total de {soma} DEU IMPAR')
    print(f'------------------------------')
    if z == 'I':
      print('Você VENCEU')
      cont += 1
      print('Vamos jogar novamente...')
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    elif z == 'P':
      print('Você PERDEU')
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
      p == False
print(f'Game Over!! Você ganhou {cont} vezes')