from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from .base_model import BaseModel
from .validators import validate_cpf, validate_data_nascimento
from .esporte import Esporte
from ..managers.atleta_manager import AtletaManager


class Atleta(BaseModel):
    """
    Modelo representando um Atleta.
    
    Attributes:
        nome: Nome completo do atleta (mínimo 5 caracteres)
        cpf: CPF do atleta (11 dígitos, único)
        email: E-mail do atleta (único)
        data_nascimento: Data de nascimento do atleta (não pode ser futura, idade mínima 12 anos)
        nacionalidade: Nacionalidade do atleta (entre 5 e 50 caracteres)
        altura: Altura do atleta em metros (entre 1.00 e 2.50)
        peso: Peso do atleta em kg (entre 30.0 e 250.0)
        esporte: Esporte praticado pelo atleta
        ativo: Indica se o atleta está ativo
    """
    nome = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(5)], 
        verbose_name='Nome'
    )
    cpf = models.CharField(
        max_length=11, 
        validators=[MinLengthValidator(11), validate_cpf], 
        unique=True, 
        verbose_name='CPF'
    )
    email = models.EmailField(
        max_length=100, 
        unique=True, 
        verbose_name='E-mail'
    )
    data_nascimento = models.DateField(
        validators=[validate_data_nascimento],
        verbose_name='Data de Nascimento'
    )
    nacionalidade = models.CharField(
        max_length=50, 
        validators=[MinLengthValidator(5)], 
        verbose_name='Nacionalidade'
    )
    altura = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(1.00), MaxValueValidator(2.50)], 
        verbose_name='Altura'
    )
    peso = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(30.0), MaxValueValidator(250.0)], 
        verbose_name='Peso (kg)'
    )
    esporte = models.CharField(
        max_length=20, 
        choices=Esporte.choices, 
        default=Esporte.NAO_ESPECIFICADO, 
        verbose_name='Esporte'
    )
    ativo = models.BooleanField(
        default=True, 
        verbose_name='Ativo'
    )
    
    # Manager customizado
    objects = AtletaManager()
    
    def __str__(self):
        """Retorna o nome do atleta e o esporte"""
        return f"{self.nome} - {self.esporte}"
    
    def clean(self):
        """Validação adicional do modelo"""
        super().clean()
        if self.data_nascimento:
            validate_data_nascimento(self.data_nascimento)