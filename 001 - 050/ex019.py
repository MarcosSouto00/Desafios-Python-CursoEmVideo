import random
n1 = input('Aluno um: ')
n2 = input('Aluno dois: ')
n3 = input('Aluno três: ')
n4 = input('Aluno quatro: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print (f'O/A Escolhido/a foi {escolhido}')