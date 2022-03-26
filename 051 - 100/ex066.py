cont = soma = 0
while True:
  x = int(input('Digite um número: '))
  if x != 999:
    cont += 1
    soma += x
  if x == 999:
    break
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')