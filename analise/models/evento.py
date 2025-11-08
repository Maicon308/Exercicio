from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel
from .esporte import Esporte
from ..managers.evento_manager import EventoManager


class Evento(BaseModel):
    """
    Modelo representando um Evento esportivo.
    
    Attributes:
        nome: Nome do evento (mínimo 5 caracteres)
        local: Local do evento (mínimo 5 caracteres)
        cidade: Cidade do evento (mínimo 2 caracteres)
        pais: País do evento (mínimo 2 caracteres)
        data: Data de realização do evento
        esporte: Esporte do evento
        oficial: Indica se é um evento oficial
        organizador: Nome do organizador (mínimo 2 caracteres)
        capacidade: Capacidade de público do evento
    """
    nome = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(5)], 
        verbose_name='Nome'
    )
    local = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(5)], 
        verbose_name="Local"
    )
    cidade = models.CharField(
        max_length=80, 
        validators=[MinLengthValidator(2)], 
        verbose_name='Cidade'
    )
    pais = models.CharField(
        max_length=80, 
        validators=[MinLengthValidator(2)], 
        verbose_name='Pais'
    )
    data = models.DateField(
        verbose_name='Data'
    )
    esporte = models.CharField(
        max_length=20, 
        choices=Esporte.choices, 
        default=Esporte.NAO_ESPECIFICADO, 
        verbose_name='Esporte'
    )
    oficial = models.BooleanField(
        default=True, 
        verbose_name='Evento Oficial'
    )
    organizador = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(2)], 
        verbose_name='Organizador'
    )
    capacidade = models.IntegerField(
        validators=[MinValueValidator(0)],  
        verbose_name='Capacidade'
    )
    
    # Manager customizado
    objects = EventoManager()
    
    def __str__(self):
        """Retorna o nome do evento, esporte, cidade, país e a data no formato DD/MM/AAAA"""
        return f"{self.nome} - {self.esporte} - {self.cidade}, {self.pais} - {self.data.strftime('%d/%m/%Y')}"