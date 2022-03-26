matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totp = c3t = maiorn = 0
for c in range(0, 3):
  for p in range(0, 3):
    x = matriz[c][p] = int(input(f'Digite um valor para a posição [{c}, {p}]: '))
    if x % 2 == 0:
      totp += x
    if p == 2:
      c3t += x
    if c == 1 and p == 0:
      maiorn = x
    elif c == 1 and p > 0:
      if x > maiorn:
        maiorn = x
  
print('-=-' * 10)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]''')
print('-=-' * 10)
print(f'A soma de todos os valores pares é {totp}')
print(f'A soma de todos os valores da 3° coluna é {c3t}')
print(f'O maior valor da 2° linha é {maiorn}')