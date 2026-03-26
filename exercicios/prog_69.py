# Crie no algoritmo 67 as seguintes funcionalidades:
# Informe ao usuário em caso de empate.
# Crie uma forma de não permitir que um jogador jogue no mesmo lugar que já tenha uma jogada realizada.
# Atualmente o jogo encerra com o vencedor, ele agora também deve encerrar em caso de empate.
# Ao finalizar o jogo deve ser informado ao usuário uma mensagem solicitando uma nova partida, o sistema de reiniciar o jogo em caso de sim, e encerrar o programa em caso de não.
# Refatore a funcionalidade que verifica a vitoria e pense em uma forma de simplificar o código corrigido.


def exibir_tabuleiro(tab):
  
    print("\n   1   2   3")
    for i in range(3):
        linha = f"{i+1}  {tab[i][0]} | {tab[i][1]} | {tab[i][2]}"
        print(linha)
        if i < 2:
            print("  -----------")

def tabuleiro_cheio(tab):

    return all(celula != ' ' for linha in tab for celula in linha)

def verificar_vitoria(tab, simbolo):

    combinacoes = [
    
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for combo in combinacoes:
        if all(tab[l][c] == simbolo for l, c in combo):
            return True
    return False

def jogar_partida():
    
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador = 1  # 1 = X, 2 = O
    simbolos = {1: 'X', 2: 'O'}
    vitoria = False
    empate = False

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"\nJogador {jogador} ({simbolos[jogador]})")
        try:
            linha = int(input("Linha (1-3): ")) - 1
            coluna = int(input("Coluna (1-3): ")) - 1
        except ValueError:
            print("entrada inválida! Use números.")
            continue

        
        if not (0 <= linha < 3 and 0 <= coluna < 3):
            print("posição fora do tabuleiro!")
            continue
        if tabuleiro[linha][coluna] != ' ':
            print("posição já ocupada! escolha outra.")
            continue

        tabuleiro[linha][coluna] = simbolos[jogador]

        if verificar_vitoria(tabuleiro, simbolos[jogador]):
            vitoria = True
            break

        if tabuleiro_cheio(tabuleiro):
            empate = True
            break

        jogador = 2 if jogador == 1 else 1

    
    exibir_tabuleiro(tabuleiro)

   
    if vitoria:
        print(f"\njogador {jogador} ganhou!")
    elif empate:
        print("\ndeu empate!")
    return vitoria, empate

def main():
    
    while True:
        jogar_partida()
        while True:
            resp = input("\ngostaria de jogar novamente? (S/N): ").strip().upper()
            if resp in ('S', 'N'):
                break
            print("\nresposta inválida. digite S ou N.")
        if resp == 'N':
            print("encerrando o jogo...")
            break

if __name__ == "__main__":
    main()