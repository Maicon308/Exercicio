from django.db import models
from datetime import date


class AtletaManager(models.Manager):
    """
    Manager customizado para o modelo Atleta com métodos de consulta específicos.
    """
    
    def buscar_corredores_vencedores(self, data: date) -> list:
        """
        Consulta atletas de corrida que ganharam alguma prova (pontuacao = 1)
        em eventos realizados desde a data informada.
        
        Args:
            data: Data a partir da qual buscar eventos
            
        Returns:
            Lista de objetos Atleta que são corredores vencedores
            
        Raises:
            ValueError: Se data for None ou inválida
        """
        if not data or not isinstance(data, date):
            raise ValueError('Data deve ser um objeto date válido')
        
        from ..models.esporte import Esporte
        
        # Buscar atletas de corrida que têm estatísticas com pontuação = 1
        # (colocação = 1º lugar) em eventos desde a data informada
        atletas = self.filter(
            esporte=Esporte.CORRIDA,
            estatisticas__pontuacao=1,
            estatisticas__evento__data__gte=data
        ).distinct()
        
        return list(atletas)
    
    def buscar_maiores_pontuadores_eventos_oficiais(self, esporte) -> models.QuerySet:
        """
        Consulta atletas que possuem a maior pontuação em eventos oficiais.
        Para corrida, a maior pontuação é o menor número (1º lugar).
        
        Args:
            esporte: Tipo de esporte (objeto Esporte)
            
        Returns:
            QuerySet de Atletas com maior pontuação em eventos oficiais
            
        Raises:
            ValueError: Se esporte for None ou inválido
        """
        if not esporte:
            raise ValueError('Esporte deve ser informado')
        
        from ..models.esporte import Esporte
        
        # Filtrar atletas do esporte em eventos oficiais
        atletas_com_stats = self.filter(
            esporte=esporte,
            estatisticas__evento__oficial=True
        ).distinct()
        
        if not atletas_com_stats.exists():
            return self.none()
        
        # Para corrida, menor pontuação é melhor (1º lugar = 1)
        if esporte == Esporte.CORRIDA:
            # Buscar a menor pontuação (melhor colocação)
            melhor_pontuacao = self.filter(
                esporte=esporte,
                estatisticas__evento__oficial=True
            ).aggregate(
                melhor=models.Min('estatisticas__pontuacao')
            )['melhor']
            
            if melhor_pontuacao is None:
                return self.none()
            
            # Retornar atletas com essa pontuação
            return self.filter(
                esporte=esporte,
                estatisticas__evento__oficial=True,
                estatisticas__pontuacao=melhor_pontuacao
            ).distinct()
        
        else:
            # Para outros esportes, maior pontuação é melhor
            melhor_pontuacao = self.filter(
                esporte=esporte,
                estatisticas__evento__oficial=True
            ).aggregate(
                melhor=models.Max('estatisticas__pontuacao')
            )['melhor']
            
            if melhor_pontuacao is None:
                return self.none()
            
            return self.filter(
                esporte=esporte,
                estatisticas__evento__oficial=True,
                estatisticas__pontuacao=melhor_pontuacao
            ).distinct()
    
    def buscar_participantes(self, evento) -> list:
        """
        Consulta os atletas que participaram de um evento específico.
        
        Args:
            evento: Objeto Evento
            
        Returns:
            Lista de objetos Atleta que participaram do evento
            
        Raises:
            ValueError: Se evento for None
        """
        if not evento:
            raise ValueError('Evento deve ser informado')
        
        # Buscar atletas que têm estatísticas neste evento
        atletas = self.filter(
            estatisticas__evento=evento
        ).distinct()
        
        return list(atletas)