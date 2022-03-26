soma = 0
cont = 0
for c in range(0, 6):
    x = int(input('Digite um número inteiro: '))
    if (x % 2) == 0:
        soma += x
        cont += 1
print(f'De 6 números {cont} foram considerados, a soma desses {cont} números deu {soma}')