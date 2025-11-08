from django.db import models
from datetime import date


class EventoManager(models.Manager):
    """
    Manager customizado para o modelo Evento com métodos de consulta específicos.
    """
    
    def buscar_evento_participantes_estrangeiros(self, data: date) -> models.QuerySet:
        """
        Consulta eventos que tiveram participantes estrangeiros desde a data informada.
        Eventos são ordenados por data de ocorrência da mais recente para a mais antiga.
        
        Um participante é considerado estrangeiro quando sua nacionalidade é diferente
        do país do evento.
        
        Args:
            data: Data a partir da qual buscar eventos
            
        Returns:
            QuerySet de Eventos com participantes estrangeiros, ordenados por data (desc)
            
        Raises:
            ValueError: Se data for None ou inválida
        """
        if not data or not isinstance(data, date):
            raise ValueError('Data deve ser um objeto date válido')
        
        # Buscar eventos desde a data informada que têm estatísticas
        # de atletas cuja nacionalidade é diferente do país do evento
        eventos = self.filter(
            data__gte=data,
            estatisticas__atleta__isnull=False
        ).exclude(
            estatisticas__atleta__nacionalidade=models.F('pais')
        ).distinct().order_by('-data')
        
        return eventos