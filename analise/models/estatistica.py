from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .base_model import BaseModel
from .validators import validate_estatistica_por_esporte, validate_atleta_idade_minima


class Estatistica(BaseModel):
    """
    Modelo representando as Estatísticas de um atleta em um evento.
    
    Attributes:
        atleta: Atleta que participou do evento
        evento: Evento em que o atleta participou
        pontuacao: Pontuação do atleta (para corrida é a colocação)
        assistencias: Número de assistências (apenas basquete e futebol)
        faltas: Número de faltas (apenas basquete e futebol)
        cartoes: Número de cartões (apenas basquete e futebol)
        minutos_jogados: Minutos jogados (apenas basquete e futebol)
        distancia: Distância percorrida (apenas corrida)
        observacoes: Observações adicionais
    """
    atleta = models.ForeignKey(
        'Atleta',
        on_delete=models.CASCADE,
        related_name='estatisticas',
        verbose_name='Atleta'
    )
    evento = models.ForeignKey(
        'Evento',
        on_delete=models.CASCADE,
        related_name='estatisticas',
        verbose_name='Evento'
    )
    pontuacao = models.IntegerField(
        validators=[MinValueValidator(0)], 
        verbose_name='Pontuação',
        null=True,
        blank=True
    )
    assistencias = models.IntegerField(
        validators=[MinValueValidator(0)], 
        verbose_name='Assistências',
        null=True,
        blank=True
    )
    faltas = models.IntegerField(
        validators=[MinValueValidator(0)], 
        verbose_name='Faltas',
        null=True,
        blank=True
    )
    cartoes = models.IntegerField(
        validators=[MinValueValidator(0)],  
        verbose_name='Cartões',
        null=True,
        blank=True
    )
    minutos_jogados = models.IntegerField(
        validators=[MinValueValidator(0)], 
        verbose_name='Minutos Jogados',
        null=True,
        blank=True
    )
    distancia = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        verbose_name='Distância',
        null=True,
        blank=True
    )
    observacoes = models.TextField(
        max_length=2000, 
        verbose_name='Observações',
        blank=True,
        default=''
    )
    
    class Meta:
        verbose_name = 'Estatística'
        verbose_name_plural = 'Estatisticas'
    
    def __str__(self):
        """Retorna o nome do atleta, nome do evento, esporte e a pontuação"""
        return f"{self.atleta.nome} - {self.evento.nome} - {self.evento.esporte} - Pontuação: {self.pontuacao}"
    
    def clean(self):
        """Validação customizada da estatística"""
        super().clean()
        
        # Validar que o atleta tem idade mínima de 12 anos
        if self.atleta and self.evento:
            validate_atleta_idade_minima(self.atleta, self.evento)
        
        # Validar que o atleta está no mesmo esporte do evento
        if self.atleta and self.evento:
            if self.atleta.esporte != self.evento.esporte:
                raise ValidationError(
                    f"O atleta pratica {self.atleta.esporte} mas o evento é de {self.evento.esporte}"
                )
        
        # Validar estatística por esporte
        if self.evento:
            validate_estatistica_por_esporte(self)
    
    def save(self, *args, **kwargs):
        """Override do save para executar validações"""
        self.full_clean()
        super().save(*args, **kwargs)