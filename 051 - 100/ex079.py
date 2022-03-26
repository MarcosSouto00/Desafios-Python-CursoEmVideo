lista = []
dec = 'S'
while dec in 'S':
  x = int(input('Digite o valor a ser adicionado: '))
  if x in lista:
    print('Falha. Valor ja atribuido')
  else:
    lista.append(x)
    print('Valor atribuido com sucesso')
  dec = input('Quer continuar[S/N]? ').upper()
lista.sort()
print(f'Os valores atribuidos foram {lista}')
