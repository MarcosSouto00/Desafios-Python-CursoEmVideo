l1 = float(input('Digite o tamanho da primeira reta '))
l2 = float(input('Digite o tamanho da segunda media '))
l3 = float(input('Digite o tamanho da terceira reta '))
if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
  print ('É possivel formar um triângulo')
  if l1 == l2 and l1 == l3 and l2 == l3:
    print ('Esse triângulo é Equilátero') 
  elif l1 != l2 and l1 == l3 and l2 != l3 or l1 != l2 and l2 == l3 and l1 != l3 or l3 != l2 and l1 == l2 and l3 != l1:
    print ('Esse triângulo é Isóceles')
  elif l1 != l2 and l1 != l3 and l2 != l3:
    print ('Esse triânglo é Escaleno')
else:
  print ('Não é possivel formar um triângulo')