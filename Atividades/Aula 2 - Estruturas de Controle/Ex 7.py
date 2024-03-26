numero = input("Informe um número de até 6 dígitos: ")

def conta(numero):
    if len(numero) > 6:
        print("Número de dígitos excede o limite de 6.")
        return

    soma = sum(int(digito) for digito in numero)
    digito_verificador = soma % 10
    numero_completo = f"{numero.zfill(6)}-{digito_verificador}"

    print("Número de conta completo:", numero_completo)

conta(numero)
