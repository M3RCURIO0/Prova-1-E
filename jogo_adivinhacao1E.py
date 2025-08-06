#Mateus Guastala Montanha
#biblioteca para gerar numero aleatorio
import random
import os
#biblioteca para limpar a tela do terminal
os.system("cls")
erros=0
sorteador=random.randint(0,100)
jogador=int(input("Digite um numero entre 0 e 100: "))
while(sorteador!=jogador): 
    os.system("cls")
    if(sorteador>jogador):
      print("O numero sorteado é maior que o numero digitado")
    elif (sorteador<jogador):
      print("O numero sorteado é menor que o numero digitado")
    erros+=1
    jogador=int(input("Digite um numero entre 0 e 100: "))
print("numero: " + str(jogador) + " , você acertou em: " + str(erros+1) + " tentativas")
