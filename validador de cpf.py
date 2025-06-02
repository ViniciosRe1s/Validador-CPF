def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(digito) * mult for digito, mult in zip(cpf_parcial, multiplicadores))
    resultado = (soma * 10) % 11
    return 0 if resultado == 10 else resultado

cpf = input("Digite os 11 dígitos do CPF (somente números): ")

if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF inválido.")
else:
    primeiro_digito = calcular_digito(cpf[:9], range(10, 1, -1))

    segundo_digito = calcular_digito(cpf[:9] + str(primeiro_digito), range(11, 1, -1))
    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        print("CPF válido.")
    else:
        print("CPF inválido.")
