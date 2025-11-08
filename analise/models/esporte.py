from django.db import models
from .base_model import models
from django.utils.translation import gettext_lazy as _

# Escolha da modalidade do atleta
class Esporte(models.TextChoices):
    FUTEBOL = "FUTEBOL", _('futebol')
    BASQUETE = "BASQUETE", _('basquete')
    CORRIDA = "CORRIDA", _('corrida')
    VOLEI = "VÔLEI", _('vôlei')
    NATACAO = "NATAÇÃO", _('natação')
    ATLETISMO = "ATLETISMO", _('atletismo')
    TENIS = "TÊNIS", _('tênis')
    NAO_ESPECIFICADO = "Não Especificado", _('não especificado')
 