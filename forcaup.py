import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvedor", "computador", "jogo", "forca"]

# Função para selecionar uma palavra aleatória da lista
def escolher_palavra(palavras):
    return random.choice(palavras).lower()

# Função para exibir o estado atual da palavra com as letras adivinhadas
def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()

# Função para exibir o boneco da forca com base nas tentativas erradas
def exibir_boneco(tentativas_erradas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(estagios[tentativas_erradas])

# Função principal do jogo da forca
def jogar_forca():
    palavra = escolher_palavra(palavras)
    letras_adivinhadas = []
    tentativas_erradas = 0
    tentativas_maximas = 6

    print("Bem-vindo ao jogo da forca!")
    
    while tentativas_erradas < tentativas_maximas:
        exibir_boneco(tentativas_erradas)
        print("\n" + exibir_palavra(palavra, letras_adivinhadas))
        print(f"Tentativas restantes: {tentativas_maximas - tentativas_erradas}")
        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
        elif letra in palavra:
            letras_adivinhadas.append(letra)
            print("Boa! A letra está na palavra.")
        else:
            letras_adivinhadas.append(letra)
            tentativas_erradas += 1
            print("Errado! A letra não está na palavra.")

        if all(letra in letras_adivinhadas for letra in palavra):
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        exibir_boneco(tentativas_erradas)
        print("\nVocê perdeu! A palavra era:", palavra)

# Executa o jogo da forca
if __name__ == "__main__":
    jogar_forca()
