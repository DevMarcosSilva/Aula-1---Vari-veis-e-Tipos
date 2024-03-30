#Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde
#você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
#posição está livre. Verifique também quando um jogador venceu a partida.
#Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual
#cada elemento é outra lista também com três elementos.

def print_tabuleiro(tabuleiro):
    """Função para imprimir o tabuleiro."""
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

def verifica_vencedor(tabuleiro, jogador):
    """Função para verificar se há um vencedor."""
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def jogo_da_velha():
    """Função principal do jogo da velha."""
    # Inicializa o tabuleiro vazio
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0

    # Loop principal do jogo
    while True:
        # Imprime o tabuleiro atual
        print("\nTabuleiro atual:")
        print_tabuleiro(tabuleiro)

        # Pede a jogada ao jogador atual
        linha = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a linha (0, 1, ou 2): "))
        coluna = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a coluna (0, 1, ou 2): "))

        # Verifica se a posição está livre
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada! Tente novamente.")
            continue

        # Marca a jogada no tabuleiro
        tabuleiro[linha][coluna] = jogadores[jogador_atual]

        # Verifica se houve um vencedor
        if verifica_vencedor(tabuleiro, jogadores[jogador_atual]):
            print(f"Parabéns! O jogador {jogadores[jogador_atual]} venceu!")
            print_tabuleiro(tabuleiro)
            break

        # Verifica se houve empate
        if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
            print("Empate!")
            print_tabuleiro(tabuleiro)
            break

        # Alterna para o próximo jogador
        jogador_atual = (jogador_atual + 1) % 2

# Executa o jogo da velha
jogo_da_velha()

