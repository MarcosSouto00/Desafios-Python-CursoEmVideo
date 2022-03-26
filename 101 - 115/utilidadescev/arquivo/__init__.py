from utilidadescev.interface import *

def arqExiste(nome):
  try:
    a = open(nome, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True
  
def arqCriar(nome):
  try:
    a = open(nome, 'wt+')
    a.close()
  except:
    print('Houve um erro')
    
def lerArq(nome):
  try:
    a = open(nome, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else:
    cabecalho('PESSOAS CADASTRADAS')
    for lin in a:
      dado = lin.split(';')
      dado[1] = dado[1].replace('\n', '')
      print(f'{dado[0]:<30}{dado[1]:>3} Anos')
  finally:
    a.close()
    
def cadastrar(arq, nome='desconhecido', idade=0):
  try:
    a = open(arq, 'at')
  except:
    print('ERRO ao executar o arquivo')
  else:
     try:
       a.write(f'{nome};{idade}\n')
     except:
       print('Erro ao adicionar dados')
     else:
       print(f'{nome} foi registrado(a) com sucesso')
       a.close