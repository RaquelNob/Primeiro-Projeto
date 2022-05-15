#Medidor de Velocidade: Levando em consideração a velocidade máxima permitida de 80Km em uma determinada rua, crie um programa que recebe do usuário um valor que representa a velocidade e diga se ele foi multado e se a multa aplicada foi leve, grave ou gravíssima. Se a pessoa estiver abaixo da velocidade máxima, o programa deve exibir "Não houve multa"; se estiver 10Km acima, exibir "Levou multa leve"; se estiver entre 11 e 20
velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print ('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print ('Levou multa leve')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print ('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print ('Levou multa gravíssima')