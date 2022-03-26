n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    if valor >= 0 and valor <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você escolheu {n[valor]}')