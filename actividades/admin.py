from django.contrib import admin
from centro_cultural.actividades.models import Monitor, UsuarioInscrito, ResponsableSala, Sala, Actividad

admin.site.register(Monitor)
admin.site.register(UsuarioInscrito)
admin.site.register(ResponsableSala)
admin.site.register(Sala)
admin.site.register(Actividad)