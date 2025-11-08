from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from .base_model import BaseModel # importa a classe BaseModel
from .validators import validate_cpf # Criei uma função de validação de cpf
from .esporte import Esporte # Enum: Lista de escolhas

# Inclusão de atletas
class Atleta(BaseModel):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(5)], verbose_name='Nome')
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11), validate_cpf], unique=True, verbose_name='CPF')
    email = models.EmailField(max_length=100, unique=True, verbose_name='E-mail')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    nacionalidade = models.CharField(max_length=50, validators=[MinValueValidator(5), MaxValueValidator(50)], verbose_name='Nacionalidade')
    altura = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.00), MaxValueValidator(2.50)], verbose_name='Altura')
    peso = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(30.0), MaxValueValidator(250.0)], verbose_name='Peso (kg)')
    esporte = models.CharField(max_length=20, choices=Esporte.choices, default=Esporte.NAO_ESPECIFICADO, verbose_name='Esporte')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    
    def __str__(self):
        return f"{self.nome} - {self.esporte}"


  




