times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino',
	        'Flamengo', 'Athletico-PR', 'Ceará SC', 'Atlético-GO',
	        'Bahia', 'Fluminense', 'Corinthians', 'Santos', 
	        'Juventude', 'Internacional', 'Cuiabá', 'São Paulo',
	        'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')
print('—' * 40)
print(f'Os 5 primeiros colocados da tabela são: {times[0:5]}')
print('—' * 40)
print(f'Os últimos 4 colocados da tabela são: {times[-4:]}')
print('—' * 40)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('—' * 40)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição da tabela')