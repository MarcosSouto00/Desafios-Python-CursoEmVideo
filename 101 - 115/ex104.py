import colorama
colorama.init(autoreset=True)

def leiaInt(num):
  while num.isnumeric() == False:
    print('\033[31mERRO! Digite um numero inteiro válido')
    num = input('Digite um número inteiro: ')
  if num.isnumeric() == True:
    return num
      
      
x = leiaInt(input('Digite um número inteiro: '))
print(f'Você digitou o número {x}')