from django.contrib import admin
from .models.atleta import Atleta
from .models.evento import Evento
from .models.estatistica import Estatistica

# Registrando os modelos na interface administrativa
admin.site.register(Atleta)
admin.site.register(Evento)
admin.site.register(Estatistica)