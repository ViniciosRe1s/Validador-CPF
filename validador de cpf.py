def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(digito) * mult for digito, mult in zip(cpf_parcial, multiplicadores))
    resultado = (soma * 10) % 11
    return 0 if resultado == 10 else resultado

# Entrada do usuário
cpf = input("Digite os 11 dígitos do CPF (somente números): ")

# Verifica se tem 11 dígitos e se todos são iguais (CPF inválido)
if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF inválido.")
else:
    # Primeiro dígito verificador
    primeiro_digito = calcular_digito(cpf[:9], range(10, 1, -1))

    # Segundo dígito verificador
    segundo_digito = calcular_digito(cpf[:9] + str(primeiro_digito), range(11, 1, -1))

    # Verifica se os dois dígitos batem com os do CPF
    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        print("CPF válido.")
    else:
        print("CPF inválido.")
