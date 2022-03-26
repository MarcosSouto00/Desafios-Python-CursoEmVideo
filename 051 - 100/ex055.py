lista = []
for c in range(0, 5):
    p = float(input('Digite um peso: '))
    lista += [p]
print(f'O maior peso é {max(lista)} e o menor é {min(lista)}')
