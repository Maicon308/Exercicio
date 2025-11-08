import re
from datetime import date
from django.core.exceptions import ValidationError


def validate_cpf(cpf: str) -> bool:
    """
    Valida um CPF (Cadastro de Pessoa Física) brasileiro.
    
    Args:
        cpf: String contendo o CPF a ser validado
        
    Returns:
        True se o CPF for válido
        
    Raises:
        ValidationError: Se o CPF for inválido
    """
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        raise ValidationError('CPF deve ter 11 dígitos')

    # Elimina CPFs com todos os dígitos iguais
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')

    # Calcula os dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if int(cpf[i]) != digito:
            raise ValidationError('CPF inválido')

    return True


def validate_data_nascimento(data_nascimento):
    """
    Valida que a data de nascimento não é futura e que o atleta tem pelo menos 12 anos.
    
    Args:
        data_nascimento: Data de nascimento a ser validada
        
    Raises:
        ValidationError: Se a data for futura ou atleta tiver menos de 12 anos
    """
    hoje = date.today()
    
    # Não permitir data futura
    if data_nascimento > hoje:
        raise ValidationError('Data de nascimento não pode ser futura')
    
    # Calcular idade
    idade = hoje.year - data_nascimento.year - (
        (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
    )
    
    # Idade mínima de 12 anos
    if idade < 12:
        raise ValidationError('Atleta deve ter no mínimo 12 anos de idade')


def validate_atleta_idade_minima(atleta, evento):
    """
    Valida que o atleta tinha pelo menos 12 anos na data do evento.
    
    Args:
        atleta: Objeto Atleta
        evento: Objeto Evento
        
    Raises:
        ValidationError: Se o atleta tiver menos de 12 anos na data do evento
    """
    data_evento = evento.data
    data_nascimento = atleta.data_nascimento
    
    # Calcular idade na data do evento
    idade_no_evento = data_evento.year - data_nascimento.year - (
        (data_evento.month, data_evento.day) < (data_nascimento.month, data_nascimento.day)
    )
    
    if idade_no_evento < 12:
        raise ValidationError(
            f'Atleta {atleta.nome} tinha {idade_no_evento} anos na data do evento. '
            'Idade mínima é 12 anos.'
        )


def validate_estatistica_por_esporte(estatistica):
    """
    Valida a estatística de acordo com o esporte.
    
    Para Corrida:
        - pontuacao (colocação) deve ser >= 1
        - distancia deve ser obrigatória e >= 1
        - assistencias, faltas, cartoes e minutos_jogados devem ser nulos
        
    Para Basquete e Futebol:
        - pontuacao, assistencias, faltas, cartoes e minutos_jogados devem ser obrigatórios e >= 0
        - distancia deve ser nula
        
    Args:
        estatistica: Objeto Estatistica
        
    Raises:
        ValidationError: Se a estatística não estiver de acordo com o esporte
    """
    from .esporte import Esporte
    
    esporte = estatistica.evento.esporte
    
    if esporte == Esporte.CORRIDA:
        # Para corrida: pontuação mínima é 1 (colocação)
        if estatistica.pontuacao is None or estatistica.pontuacao < 1:
            raise ValidationError('Para corrida, a pontuação (colocação) deve ser no mínimo 1')
        
        # Distância obrigatória e mínimo 1
        if estatistica.distancia is None or estatistica.distancia < 1:
            raise ValidationError('Para corrida, a distância é obrigatória e deve ser no mínimo 1')
        
        # Campos que devem ser nulos
        if any([
            estatistica.assistencias is not None,
            estatistica.faltas is not None,
            estatistica.cartoes is not None,
            estatistica.minutos_jogados is not None
        ]):
            raise ValidationError(
                'Para corrida, assistências, faltas, cartões e minutos jogados devem ser nulos'
            )
    
    elif esporte in [Esporte.BASQUETE, Esporte.FUTEBOL]:
        # Todos os campos obrigatórios e mínimo 0
        campos_obrigatorios = {
            'pontuacao': estatistica.pontuacao,
            'assistencias': estatistica.assistencias,
            'faltas': estatistica.faltas,
            'cartoes': estatistica.cartoes,
            'minutos_jogados': estatistica.minutos_jogados
        }
        
        for nome_campo, valor in campos_obrigatorios.items():
            if valor is None:
                raise ValidationError(
                    f'Para {esporte}, o campo {nome_campo} é obrigatório'
                )
            if valor < 0:
                raise ValidationError(
                    f'Para {esporte}, o campo {nome_campo} deve ser no mínimo 0'
                )
        
        # Distância deve ser nula
        if estatistica.distancia is not None:
            raise ValidationError(
                f'Para {esporte}, o campo distância deve ser nulo'
            )