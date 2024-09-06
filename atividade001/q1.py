import random

armazenar_numeros = []


def lancar_dado():
    resultado = random.randint(1, 6)
    return resultado


for i in range(100):
    numero = lancar_dado()
    armazenar_numeros.append(numero)


def main():
    contador = 0
    for c in range(1, 7):
        contador = armazenar_numeros.count(c)
        print(f"O número {c} apareceu {contador} vezes em 100 lançamentos.")
    return contador


if __name__ == "__main__":
    main()
