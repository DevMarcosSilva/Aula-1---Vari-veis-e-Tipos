#faça um jogo da Forca utilizando listas. Dada uma palavra, dê algumas
#chances para o usuário acertar.
import random

def escolher_palavra():
    
    palavras = ['python', 'programação', 'computador', 'algoritmo', 'desenvolvimento']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    
    exibicao = ''
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def desenhar_boneco(tentativas):
    
    if tentativas == 6:
        print("""
          +---+
              |
              |
              |
              |
              |
        =========
        """)
    elif tentativas == 5:
        print("""
          +---+
          |   |
              |
              |
              |
              |
        =========
        """)
    elif tentativas == 4:
        print("""
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """)
    elif tentativas == 3:
        print("""
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """)
    elif tentativas == 2:
        print("""
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """)
    elif tentativas == 1:
        print("""
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """)
    elif tentativas == 0:
        print("""
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        """)

def jogo_da_forca():
    
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas = 6

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra:")

    while tentativas > 0:
        exibicao = exibir_palavra(palavra, letras_corretas)
        print("\nPalavra:", exibicao)

        if '_' not in exibicao:
            print("Parabéns! Você adivinhou a palavra!")
            break

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print("Correto! Esta letra está na palavra.")
        else:
            tentativas -= 1
            print("Incorreto! Esta letra não está na palavra. Você tem", tentativas, "tentativas restantes.")
            desenhar_boneco(tentativas)

    if tentativas == 0:
        print("Você perdeu! A palavra correta era:", palavra)

jogo_da_forca()
