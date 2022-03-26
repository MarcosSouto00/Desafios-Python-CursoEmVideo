from random import shuffle
n1 = input('Aluno um: ')
n2 = input('Aluno dois: ')
n3 = input('Aluno tres: ')
n4 = input('Aluno quatro: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print (f'A ordem será \n{lista}') 