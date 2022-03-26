lista = []
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > max(lista):
        lista.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        for p, c in enumerate(lista):
           if num <= c:
               lista.insert(p, num)
               print(f'Valor adicionado na posição {p} da lista...')
               break
print(f'Os valores digitados em ordem foram {lista}')