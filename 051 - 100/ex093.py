dados = {}
p = []
tot = 0
cont = 1
dados['Nome'] = input('Nome: ')
n = int(input('Quantas partidas ele jogou? '))
for c in range(1, n+1):
  x = int(input(f'Quantos gols ele fez no jogo {c}: '))
  p.append(x)
  tot += x
dados['Gols'] = p[:]
dados['Total'] = tot
print('-=-' * 15)
for k, v in dados.items():
  print(f'{k}: {v}')
print('-=-' * 15)
print(f'O Jogador {dados["Nome"]} jogou {n} jogos')
for i, v in enumerate(dados['Gols']):
  print(f'  =>No jogo {cont}, ele fez {v} gols')
  cont += 1
print(f'Fez um total de {dados["Total"]} gols')
