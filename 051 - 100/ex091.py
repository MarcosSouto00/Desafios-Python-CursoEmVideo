from random import randint
from time import sleep
from operator import itemgetter

jogo = {'p1': randint(1, 6),
        'p2': randint(1, 6),
        'p3': randint(1, 6),
        'p4': randint(1, 6)}
for k, v in jogo.items():
  print(f'O {k} Tirou {v}')
  sleep(1)
rank = []
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
  print(f'{i+1}° lugar: {v[0]} com {v[1]}')
  sleep(1)