dic = {}
dic['nome'] = input('Nome: ')
dic['media'] = float(input('Média: '))
print(f'Nome: {dic["nome"]}')
print(f'Média: {dic["media"]}')
if dic['media'] >= 7.0:
  print(f'Situação: Aprovado')
else:
  print(f'Situação: Reprovado')