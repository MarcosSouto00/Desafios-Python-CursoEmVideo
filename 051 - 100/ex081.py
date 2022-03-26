lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opção = ' '
    while opção not in 'SsNn':
        opção = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break
lista.sort(reverse = True)
print('—' * 30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
  print('O valor 5 foi atribuido')
else:
  print('O valor 5 não foi atribuido')
