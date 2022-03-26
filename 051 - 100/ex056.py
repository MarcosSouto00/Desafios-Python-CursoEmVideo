maisvelho = 0
mulhermenor = 0
somaidade = 0
nomevelho = ''
for c in range(1, 5):
  print (f'--------{c}° PESSOA--------')
  nome = input('Nome: ')
  idade = int(input('Idade: '))
  sexo = input('Sexo[M/F]: ').upper()
  somaidade += idade
  if c == 1 and sexo == 'M':
    maisvelho = idade
    nomevelho = nome
  if sexo == 'M' and idade > maisvelho:
    maisvelho = idade
    nomevelho = nome
  if sexo == 'F':
    if idade < 20:
      mulhermenor += 1
print(f'A média de idade do grupo é de {somaidade / 4}')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomevelho}')
print(f'Ao todo são {mulhermenor} mulheres com menos de 20 anos')