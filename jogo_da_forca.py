print("********************")
print("***JOGO DA FORCA!***")
print("********************")

palavra_secreta = "banana"
letras_acertadas = ["_","_","_","_","_","_"]

enforcou = False    
acertou = False

print(letras_acertadas)

while (not acertou and not enforcou):
    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if (chute.upper == letra.upper):
            letras_acertadas[index] = letra
        index += 1
    
    print(letras_acertadas)
    
    letras_faltando = str(letras_acertadas.count("_"))
    if (letras_faltando == False):
        print("VOCÊ GANHOU!")
    else: 
        print("Estão faltando {} letras.".format(letras_faltando))
    

    print("Jogando...")

print("Fim do Jogo.")

# .upper para passar as letras para caixa alta
# .lower para passar as letras para caixa baixa 
# .catalize para somente a primeira letra em caixa alta

# ***Para criar uma lista***
# nome_da_list = [] (já podem ser colocados val na sua inicialização)

# ***Para saber seu valor mínimo e máximo***
# min(nome_da_lista)
# max(nome_da_lista)

# ***Para saber o tamanho da lista***
# print (len(letras_acertadas))
# 6

# ***Para resgatar determinado valor da lista***
# nome_da_lista = [0, 1, 2, 3]
# [2]
# 2

# ***Para verificar se há determinado valor***
# valores[0, 1, 2, 3]
# 0 in valores
# True
# 8 in valores
# False
