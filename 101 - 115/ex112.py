from utilidadescev import moeda, dados

p = str(dados.leiaDinheiro(input('Digite um valor: ')))
moeda.resumo(int(p), 80, 35)