def ficha(nome='desconhecido', gol=0):
  return f'O jogador {nome} fez {gol} gol(s)'

nome = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')

if gols.isnumeric() == False:
  gols = 0

else:
  gols = int(gols)


#if nome.isalnum() == True or nome.isalpha() == True or nome.isnumeric() == True
if nome.strip() != '':
  x = ficha(nome, gols)

else:
  x = ficha(gol=gols)

print(x)