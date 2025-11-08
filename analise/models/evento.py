from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from .esporte import Esporte

# Informações do evento
class Evento(BaseModel):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(5)], verbose_name='Nome')
    local = models.CharField(max_length=100, validators=[MinLengthValidator(5)], verbose_name="Local")
    cidade = models.CharField(max_length=80, validators=[MinLengthValidator(2)], verbose_name='Cidade')
    pais = models.CharField(max_length=80, validators=[MinLengthValidator(2)], verbose_name='Pais')
    data = models.DateField(verbose_name='Data de Nascimento')
    esporte = models.CharField(max_length=20, choices=Esporte.choices, default=Esporte.NAO_ESPECIFICADO, verbose_name='Esporte')
    oficial = models.BooleanField(default=True, verbose_name='Evento Oficial')
    organizador = models.CharField(max_length=100, validators=[MinLengthValidator(2)], verbose_name='Organizador')
    capacidade = models.IntegerField(validators=[MinValueValidator(0)],  verbose_name='Capacidade')
    
    def __str__(self):
        return f"{self.nome} ({self.cidade}, {self.pais})"


