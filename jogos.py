import random

import forca
import adivinhacao

def escolhe_jogo():
  print("Escolha seu jogo!")
  
  print ("(1) Forca (2) Adivinhação")
  
  jogo = int(input("Qual jogo? "))
  
  if (jogo == 1):
    forca.jogar()
  
  elif (jogo == 2):
    adivinhacao.jogar()
  
  else:
    print("Opção inválida")

if (__name__ == "__main__"):
  escolhe_jogo()