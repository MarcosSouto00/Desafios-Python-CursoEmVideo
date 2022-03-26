nome = input('Digite uma palavra: ').upper()
print (f'A letra A aparece {nome.count("A")} vezes')
print (f'Ele aparece pela primeira vez na posição {nome.find("A")+1}')
print (f'E pela ultima vez na posição {nome.rfind("A")+1}')