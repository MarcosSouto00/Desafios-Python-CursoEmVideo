import urllib
import urllib.request

try:
  site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
  print('Não consegui acessar o site Pudim')
else:
  print('Consegui acessar o site Pudim com sucesso')