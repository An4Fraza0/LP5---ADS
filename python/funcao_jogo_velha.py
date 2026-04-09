tabuleiro =[0, 1, 2, 3, 4, 5, 6, 7, 8]

def desenhar_tabuleiro():
    print(tabuleiro[0], tabuleiro[1], tabuleiro[2])
    print(tabuleiro[3], tabuleiro[4], tabuleiro[5])
    print(tabuleiro[6], tabuleiro[7], tabuleiro[8])


def jogar(jogada, jogador):
    tabuleiro[jogada] = jogador


def verificar_jogada(jogada):
    if tabuleiro[jogada] == "X" or tabuleiro[jogada] == "O":
        print("jogada inválida, tente novamente")
        return False
    else:
        return True
    

def verificar_vencedor(tabuleiro):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),  # linhas
        (0,3,6), (1,4,7), (2,5,8),  # colunas
        (0,4,8), (2,4,6)            # diagonais
    ]
    for combinacao in combinacoes:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] != ' ':
            return tabuleiro[combinacao[0]]
    return None



