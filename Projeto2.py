#Chute o número: Crie um programa que, ao iniciar, gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado seja chutado corretamente.
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute foi maoir que o valor gerado')
  elif chute < valor_aleatorio:
    print('Chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou!')