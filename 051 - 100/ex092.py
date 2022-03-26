dados = {}
dados['Nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho [0 se não tiver]: '))
dados['Idade'] = 2022 - ano
if dados['CTPS'] != 0:
  dados['Contratação'] = int(input('Ano de Contratação: '))
  dados['Salário'] = float(input('Salário: '))
  dados['Aposentadoria'] = (dados['Contratação'] - ano) + 35
print('-=-' * 15)
for k, v in dados.items():
  print(f'{k}: {v}')