cnt = 'S'
y = 0
lista = []
cont = 0
while cnt == 'S':
  x = int(input('Digite um número: '))
  cnt = str(input('Quer continuar[S/N]? ')).upper()
  y += x
  lista += [x]
  cont += 1
print(f'Você digitou {cont} números, a media entre eles é {y / cont}\nO maior valor foi {max(lista)} e o menor foi {min(lista)}')