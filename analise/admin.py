from django.contrib import admin

from .models.atleta import Atleta
from .models.estatistica import Estatistica
from .models.esporte import Esporte
from .models.evento import Evento

# Register your models here.

admin.site.register(Atleta)
admin.site.register(Estatistica)
admin.site.register(Evento)