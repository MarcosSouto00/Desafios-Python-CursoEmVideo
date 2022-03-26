l1 = l2 = l3 = []
while True:
    l1.append(int(input('Digite um valor: ')))
    opção = ' '
    while opção not in 'SsNn':
        opção = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break
for num in l1:
  if num % 2 == 0:
    l2.append(num)
  else:
    l3.append(num)
print(f'A lista completa é {l1}')
print(f'A lista de pares é {l2}')
print(f'A lista de impares é {l3}')