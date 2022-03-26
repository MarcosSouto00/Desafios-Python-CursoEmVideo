total = [[], []]
for c in range(1, 8):
  x = int(input(f'Digite o {c}° Valor: '))
  if x % 2 == 0:
    total[0].append(x)
  else:
    total[1].append(x)
total[0].sort()
total[1].sort()
print(f'Os valores pares digitado foram {total[1]}')
print(f'Os valores impares digitado foram {total[0]}')