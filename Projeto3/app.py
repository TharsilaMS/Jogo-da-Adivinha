# Jogo da Adivinhação
# Desenvolva um programa simples em Python que permita ao usuário adivinhar um número secreto. 
# O programa deve fornecer dicas ao usuário para ajudá-lo a acertar o número.

import random
def adivinhacao():
 
 num_correto = random.randint(1,8)

 while True:
   try:
    max_tentativa = int(input("Digite quantas tentativas você deseja! "))
    if max_tentativa <= 0:
     print("O número não pode ser uma letra nem 0 ou menor ")
     continue
    break
     
   except ValueError:
            print("Digite um número válido!")

 num_tentativa =0

 while True:
      
    num_tentativa = num_tentativa + 1
    if num_tentativa > max_tentativa:
        print(f"Você atingiu o maxímo de tentativas o nùmero correto era {num_correto}")
        break
    try:
        num = int(input("Digite o número que você acha que é : \n"))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue
    if num == num_correto:
        print(f"Você acertou o número correto é {num_correto} o seu número de tentativas foi {num_tentativa}")
        break
    elif num < num_correto:
        print("O número que você digitou é menor que o número correto! \n")
    elif num > num_correto:
        print("O número que você digitou é maior que o número correto! \n " )
    
adivinhacao()