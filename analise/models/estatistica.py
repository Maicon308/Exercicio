from django.db import models
from .base_model import BaseModel # Import da classe BaseModel
from django.core.validators import MinValueValidator, MaxLengthValidator

# Relatório do evento
class Estatistica(BaseModel):
    pontuacao = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Pontuação')
    assistencias = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Assistências')
    faltas = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Faltas')
    cartoes = models.IntegerField(validators=[MinValueValidator(0)],  verbose_name='Cartões')
    minutos_jogados = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Minutos Jogados')
    distancia = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Distância')
    observacoes = models.TextField(max_length=2000, verbose_name='Observações')
    
    class Meta:
        verbose_name = 'Estatística'
        verbose_name_plural = 'Estatisticas'
    
    def __str__(self):
        return f"Estatística (Pontuação: {self.pontuacao}, Assistências: {self.assistencias})"



