def verificar_palindromo(texto):
    texto_limpo = ""
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere.lower()
    return texto_limpo == texto_limpo[::-1]


def main():
    frase = input("Informe uma palavra ou frase para verificação: ")
    if verificar_palindromo(frase):
        print(f"'{frase}' é um palíndromo.")
    else:
        print(f"'{frase}' não é um palíndromo.")


if __name__ == "__main__":
    main()
