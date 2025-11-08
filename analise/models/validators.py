import re

def validate_cpf(cpf: str) -> bool:
    """
    Valida um CPF (Cadastro de Pessoa Física) brasileiro.

    Retorna True se o CPF for válido, False caso contrário.
    """
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Elimina CPFs com todos os dígitos iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if int(cpf[i]) != digito:
            return False

    return True
