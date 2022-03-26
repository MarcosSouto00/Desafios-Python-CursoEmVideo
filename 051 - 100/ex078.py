lista = []

for c in range(0, 5):
  lista.append(int(input(f'Digite um valor para a posição {c}: ')))

print('=-=' * 10)

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado é o {max(lista)} e ele está na posição {lista.index(max(lista))}')
print(f'O menor valor digitado é o {min(lista)} e ele está na posição {lista.index(min(lista))}')