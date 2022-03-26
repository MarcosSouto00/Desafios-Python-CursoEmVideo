mais18 = homens = mulher = 0
while True:
    print ('—' * 22)
    print (' CADASTRE UMA PESSOA')
    print ('—' * 22)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip()[0]
    opção = ' '
    while opção not in 'SsNn':
        opção = str(input('Quer continuar? [S/N] ')).strip()[0]
    if idade > 18:
        mais18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if opção in 'Nn':
        break        
print (f'Foram cadastradas {mais18} pessoas com mais de 18 anos.')
print (f'Ao todo temos {homens} homems cadastrados.')
print (f'E temos {mulher} mulheres com menos de 20 anos.')