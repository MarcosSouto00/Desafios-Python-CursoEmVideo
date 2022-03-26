tot = 0
nomep = []
nomel = []
dadost = []
pesop = 0
pesol = 100000000000000000000 ** 10000
while True:
  dadost.append(input('Nome: '))
  dadost.append(float(input('Peso: ')))
  tot += 1
  if dadost[1] >= pesop:
    if dadost[1] == pesop:
      nomep.append(dadost[0])
    elif dadost[1] > pesop:
      nomep.clear()
      nomep.append(dadost[0])
      pesop = dadost[1]
  if dadost[1] <= pesol:
    if dadost[1] == pesol:
      nomel.append(dadost[0])
    elif dadost[1] < pesol:
      pesol = dadost[1]
      nomel.clear()
      nomel.append(dadost[0])
  dadost.clear()
  opção = str(input('Quer continuar? [S/N]: ')).strip()[0]
  if opção in 'Nn':
    break

print(f'O total de pessoas cadastradas foi {tot}')
print(f'O maior peso registrado foi de {pesop}KG. peso de {nomep}')
print(f'O menor peso registrado foi de {pesol}KG. peso de {nomel}')