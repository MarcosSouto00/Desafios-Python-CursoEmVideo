while True:
  x = int(input('Você quer ver a tabuada de qual valor? '))
  if x > 0:
    print('------------------------')
    print(f'{x} X 1 = {x * 1}')
    print(f'{x} X 2 = {x * 2}')
    print(f'{x} X 3 = {x * 3}')
    print(f'{x} X 4 = {x * 4}')
    print(f'{x} X 5 = {x * 5}')
    print(f'{x} X 6 = {x * 6}')
    print(f'{x} X 7 = {x * 7}')
    print(f'{x} X 8 = {x * 8}')
    print(f'{x} X 9 = {x * 9}')
    print(f'{x} X 10 = {x * 10}')
    print('------------------------')
  elif x < 0:
    break