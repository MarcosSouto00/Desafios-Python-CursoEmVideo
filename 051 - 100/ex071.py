c50 = c20 = c10 = c1 = 0
dinheiro = int(input('Digite a quantidade de dinheiro que quer sacar: '))
while dinheiro >= 50:
  dinheiro -= 50
  c50 += 1
while 20 <= dinheiro < 50:
  dinheiro -= 20
  c20 += 1
while 10 <= dinheiro < 20:
  dinheiro -= 10
  c10 += 1
while 1 <= dinheiro < 10:
  dinheiro -= 1
  c1 += 1
print(f'Você receberá {c50} notas de 50, {c20} notas de 20, {c10} notas de 10 e {c1} notas de 1 real')