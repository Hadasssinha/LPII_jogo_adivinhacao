import random

def jogar():

  print ("***************************")
  print ("****JOGO DE ADIVINHAÇÃO****")
  print ("***************************")

  numero_secreto = random.randrange(1, 100)
  total_de_tentativas = 3
  rodada = 1
  pontos = 100

  print("Qual o nível de dificuldade?")
  print("(1) Fácil (2) Médio (3) Difícil")

  nivel = int(input("Defina o nível: "))

  if (nivel == 1):
      total_de_tentativas = 20
  elif (nivel == 2):
      total_de_tentativas = 10
  else:
      total_de_tentativas = 5

  for rodada in range (1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format (rodada, total_de_tentativas))
    chute = input ("Digite o seu número entre 1 e 100: ")
    print ("Você digitou: ", chute)
    aposta = int(chute)

    if (aposta < 1 or aposta > 100):
      print ("Você deve digitar um número entre 1 e 100.")
      continue

    acertou = numero_secreto == aposta
    maior = aposta > numero_secreto
    menor = aposta < numero_secreto

    if (acertou):
      print("Você acertou e fez {} pontos!".format(pontos))
      break
    
    else:
      if (maior):
        print("Errou! Chute maior que o sorteado.")

      elif (menor):
        print("Errou! Chute menor que o sorteado.")

    if total_de_tentativas == 3:
      print (numero_secreto)

      pontos_perdidos = abs(numero_secreto - aposta)
      pontos = pontos - pontos_perdidos
      print ("ola")

    rodada = rodada + 1

if (__name__ == "__main__"):
      jogar()


    