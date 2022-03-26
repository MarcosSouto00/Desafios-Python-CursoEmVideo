from tkinter import N


nome = input('digite seu nome ')
separado = (nome.split())
junto = (''.join(separado))
print (f'{nome.upper()}\n{nome.lower()}\n{len(junto)}\n{len(separado[0])}')

