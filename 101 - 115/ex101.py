def voto(ano):
  idade = 2022 - ano
  if idade < 16:
    print(f'Com {idade} NÃO PODE VOTAR')
  elif 18 > idade >= 16 or idade >= 65 :
    print(f'Com {idade} O VOTO É OPCIONAL')
  elif 65 > idade >= 18:
    print(f'Com {idade} O VOTO É OBRIGATORIO')


voto(int(input('Digite o Ano de nascimento: ')))