total = mais1000 = maisbarato = cont = 0
nomebarato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        mais1000 += 1
    if cont == 1:
        maisbarato = preço
        nomebarato = produto
    else:
        if preço < maisbarato:
            maisbarato = preço
            nomebarato = produto
    opção = ' '
    while opção not in 'SsNn':
        opção = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break
print (f'O total da compra foi R${total:.2f}')
print (f'Temos {mais1000} produto custando mais de R$1000.00')
print (f'O produto mais barato foi {nomebarato} que custa R${maisbarato:.2f}')