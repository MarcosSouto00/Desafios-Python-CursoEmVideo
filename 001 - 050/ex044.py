valor = float(input('Digite o valor do produto: '))
print ('[ 1 ] À vista no dinheiro/cheque - 10% de desconto')
print ('[ 2 ] À vista no cartâo - 5% de desconto')
print ('[ 3 ] 2x no cartâo - Preço normal')
print ('[ 4 ] 3x ou mais no cartão - 20% de juros ')
escolha = int(input('Escolha sua forma de pagamento: '))
if escolha == 1:
  print (f'Você terá que pagar R${valor * 0.90}')
elif escolha == 2:
  print (f'Você terá que pagar R${valor * 0.95}')
elif escolha == 3:
  print (f'Você pagará 2 parcelas de R${valor / 2}')
elif escolha == 4:
  parcelas = int(input('Digite a quantidade de parcelas que você quer pagar: '))
  print (f'Você pagará {parcelas} parcelas de R${(valor * 1.20) / parcelas}')
else:
  print ('Escolha inválida, tente novamente.')