def notas(*notas, sit=False):
  """
  notas = notas dos alunos(aceita varias)
  sit(opcional) = fala a situação da sala
  retur = retorna um dicionario com os dados
  """
  cont = total = 0
  maior = ''
  menor = ''
  for n in notas:
    cont += 1
    if cont == 1:
      maior = n
      menor = n
    if n > maior:
      maior = n
    if n < menor:
      menor = n
    total += n
  media = total / cont
  dic = {}
  dic['total'] = cont
  dic['maior'] = maior
  dic['menor'] = menor
  dic['média'] = media
  if sit == True:
    if media >= 7:
      dic['situação'] = 'Boa'
    elif 7 > media >= 5:
      dic['situação'] = 'Razoavel'
    elif 5 > media:
      dic['situação'] = 'Ruim'
  return dic


resp = notas(10, 5, 6, sit=True)
print(resp)