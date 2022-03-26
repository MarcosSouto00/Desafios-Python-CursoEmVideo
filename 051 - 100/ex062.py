n1 = int(input('DIGITE O VALOR DO PRIMEIRO TERMO: '))
n2 = int(input('DIGITE O VALOR DA RAZÃO P.A: '))
i = 0
f = 10

while i < f:
    print(n1, ' => ' if i < f - 1 else ' => PAUSA \n', end='')
    n1 += n2
    i += 1
    if i == f:
        termos = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS? '))
        if termos != 0:
            i = f
            f = f + termos
        else:
            print('VOCÊ SOLICITOU {} TERMOS.'.format(f))
            print('FIM')