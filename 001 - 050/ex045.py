from random import choice


print ('Vamos jogar Pedra, Papel e Tesoura')
print ('[ R ] Pedra')
print ('[ P ] Papel')
print ('[ S ] Tesoura')
escolha = str(input('Escolha sua ação: '))
lista = ['R,' 'P', 'S']
bot = choice(lista)
if escolha == 'R':
  if bot == 'R':
    print (f'O Bot escolheu {bot}, Vocês Empataram')
  elif bot == 'P':
    print (f'O Bot escolheu {bot}, Você Perdeu')
  elif bot == 'S':
    print (f'O Bot escolheu {bot}, Você Ganhou')
elif escolha == 'P':
  if bot == 'P':
    print (f'O Bot escolheu {bot}, Vocês Empataram')
  elif bot == 'S':
    print (f'O Bot escolheu {bot}, Você Perdeu')
  elif bot == 'R':
    print (f'O Bot escolheu {bot}, Você Ganhou')
elif escolha == 'S':
  if bot == 'S':
    print (f'O Bot escolheu {bot}, Vocês Empataram')
  elif bot == 'R':
    print (f'O Bot escolheu {bot}, Você Perdeu')
  elif bot == 'P':
    print (f'O Bot escolheu {bot}, Você Ganhou')
else:
  print ('Escolha inválida. Tente novamente.')