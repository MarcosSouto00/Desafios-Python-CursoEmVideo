from time import sleep
from utilidadescev.interface import *
from utilidadescev.arquivo import *
import colorama
colorama.init(autoreset=True)

arq = 'cev.txt'

if not arqExiste(arq):
  arqCriar(arq)

while True:
  resposta = menu(['Ver Pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
  if resposta == 1:
    lerArq(arq)
  elif resposta == 2:
    nome = input('Nome: ')
    idade = leiaInt('Idade: ')
    cadastrar(arq, nome, idade)
  elif resposta == 3:
    cabecalho('Saindo do Sistema... Até Logo')
    break
  else:
    print('\033[31mERRO!! Digite uma opção válida')
  sleep(2)