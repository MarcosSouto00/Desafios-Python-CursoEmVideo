novo = 0
maior = 0
for c in range(1, 8):
  ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
  if (2022 - ano) <= 20:
    novo += 1
  else:
    maior += 1
print (f'Ao todo temos {novo} pessoas menores, e {maior} pessoas maiores')