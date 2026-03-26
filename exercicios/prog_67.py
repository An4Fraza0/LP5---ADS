# desenvolva um jogo da velha em python que funcione no terminal

def exibir_tabuleiro(tab):
    print("\n   1   2   3")
    for i in range(3):
        print(f"{i+1}  {tab[i][0]} | {tab[i][1]} | {tab[i][2]}")
        if i < 2:
            print("  -----------")

def verificar_vitoria(tab, jogador):
    simbolo = 'X' if jogador == 1 else 'O'
    
    for i in range(3):
        if all(tab[i][j] == simbolo for j in range(3)):
            return True
    
    for j in range(3):
        if all(tab[i][j] == simbolo for i in range(3)):
            return True
    
    if all(tab[i][i] == simbolo for i in range(3)):
        return True
    if all(tab[i][2-i] == simbolo for i in range(3)):
        return True
    return False

def tabuleiro_cheio(tab):
    return all(tab[i][j] != ' ' for i in range(3) for j in range(3))

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador = 1
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"\njogador {jogador} ({'X' if jogador == 1 else 'O'})")
        try:
            linha = int(input("Linha (1-3): ")) - 1
            coluna = int(input("Coluna (1-3): ")) - 1
        except ValueError:
            print("entrada inválida... use números.")
            continue

        if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = 'X' if jogador == 1 else 'O'
            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print(f"\njogador {jogador} ganhou!")
                break
            elif tabuleiro_cheio(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("\ndeu empate!")
                break
            else:
                jogador = 2 if jogador == 1 else 1
        else:
            print("jogada inválida! posição ocupada ou fora do tabuleiro.")

if __name__ == "__main__":
    jogo_da_velha()