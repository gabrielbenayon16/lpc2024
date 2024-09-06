unidades = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
dez_a_dezenove = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]


num = int(input("Informe um número até 99: "))

def main():
    if 0 <= num <= 9:
        print(unidades[num])
    elif 10 <= num <= 19:
        print(dez_a_dezenove[num - 10])
    elif 20 <= num <= 99:
        dezena = num // 10
        unidade = num % 10
        if unidade == 0:
            print(dezenas[dezena])
        else:
            print(f"{dezenas[dezena]} e {unidades[unidade]}")
    else:
        print("Número inválido.")


if __name__ == "__main__":
    main()
