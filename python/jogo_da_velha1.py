import os
from funcao_jogo_velha import desenhar_tabuleiro, jogar, verificar_jogada, verificar_vencedor, tabuleiro

vencedor = False
desenhar_tabuleiro()
contador = 1
jogador = "X"

while vencedor == False:

    jogada = int(input("\nonde deseja jogar?"))
    os.system("cls")

    retorno = verificar_jogada(jogada)

    if retorno == True:
        jogar(jogada, jogador)   

    if retorno == False:
        print("jogada inválida, tente novamente")
        contador += 1

    desenhar_tabuleiro()

    venceu = verificar_vencedor(tabuleiro)
    if venceu != None:
        print(f"o jogador {venceu} venceu")
        vencedor = True

    contador += 1
    if contador %2 == 0:
        jogador = "O"
    else: 
        jogador = "X"

    
