from random import choice


def ler_palavras(arquivo):
    with open(arquivo, 'r') as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip().upper() for palavra in palavras]


def escolher_palavra(palavras):
    return choice(palavras)


def exibir_acertos(palavra, letras_certas):
    progresso = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    return progresso


def jogo_da_forca():
    palavras = ler_palavras(r'C:\PastaTeste\PalavrasForca.txt')
    palavra_forca = escolher_palavra(palavras)
    letras_certas = set()
    letras_erradas = set()
    tentativas_max = 6

    print(f"""Bem-vindo ao jogo da forca!
Tema: Países
""")

    while tentativas_max > 0:
        print(f"\nPalavra: {exibir_acertos(palavra_forca, letras_certas)}")
        print(f"Erros: {len(letras_erradas)} de 6 / Letras erradas: {' '.join(letras_erradas)}")

        letra = input("Digite uma letra: ").upper()

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente uma diferente.")
            continue

        if letra in palavra_forca:
            letras_certas.add(letra)
            if set(palavra_forca) == letras_certas:
                print(f"\nParabéns! Você adivinhou a palavra: {palavra_forca}")
                break
        else:
            letras_erradas.add(letra)
            tentativas_max -= 1
            print(f"-> Você errou {len(letras_erradas)} vezes seguidas! Tente de novo!")

    if tentativas_max == 0:
        print(f"\nVocê perdeu! A palavra era: {palavra_forca}")


if __name__ == "__main__":
    jogo_da_forca()
