dias = int(input('Quantos dias você está com o carro? '))
km = float(input('Quantos KM você correu com o carro? '))
print (f'Você terá que pagar R${(dias*60)+(km*0.15):.2f} pelo aluguel do carro')