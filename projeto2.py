import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('chute um numero de 1 a 10'))
  if chute > valor_aleatorio:
    print('chute foi maior que o valor gerado')
  elif chute < valor_aleatorio:
    print('chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('você acertou')