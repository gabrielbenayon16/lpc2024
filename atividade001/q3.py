cpf_usuario = str(input("Digite seu CPF: "))


def verificar_tamanho():
    if len(cpf_usuario) == 14:
        return True
    else:
        return False


def verificar_pontos():
    if cpf_usuario[3] == "." and cpf_usuario[7] == ".":
        return True
    else:
        return False


def verificar_hifen():
    if cpf_usuario[11] == "-":
        return True
    else:
        return False


def calculo_primeiro_digito_verificador():
    cpf_limpo = cpf_usuario.replace("-", "").replace(".", "")
    soma1 = 0
    soma2 = 0
    for i in range(9):
        resultado1 = int(cpf_limpo[i]) * (i + 1)
        soma1 += resultado1
    resto1 = soma1 % 11
    primeiro_digito = resto1
    if primeiro_digito > 9:
        primeiro_digito = 0

    for i in range(10):
        resultado2 = int(cpf_limpo[i]) * (i)
        soma2 += resultado2
    resto2 = soma2 % 11
    segundo_digito = resto2
    if segundo_digito > 9:
        segundo_digito = 0
    return str(primeiro_digito) + str(segundo_digito)


def validar_digitos():
    if not verificar_pontos() and verificar_hifen() and verificar_tamanho():
        return False
    digitos_calculados = calculo_primeiro_digito_verificador()
    digitos_informados = cpf_usuario[12] + cpf_usuario[13]
    return digitos_calculados == digitos_informados


def main():
    if validar_digitos():
        print("CPF válido!")
    else:
        print("CPF inválido!")


if __name__ == "__main__":
    main()
