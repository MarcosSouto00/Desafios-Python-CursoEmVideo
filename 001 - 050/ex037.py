x = int(input('Digite um número inteiro: '))
print ('[ 1 ] Converter para BINÁRIO')
print ('[ 2 ] Converter para OCTAL')
print ('[ 3 ] Converter para HEXADECIMAL')
escolha = int(input('Escolha: '))
if escolha == 1:
  print (f'{x} convertido para BINÁRIO é igual a {bin(x)[2:]}')
elif escolha == 2:
  print (f'{x} convertido para BINÁRIO é igual a {oct(x)[2:]}')
elif escolha == 3:
  print (f'{x} convertido para BINÁRIO é igual a {hex(x)[2:]}')