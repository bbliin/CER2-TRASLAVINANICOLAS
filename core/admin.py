from django.contrib import admin
from .models import Solicitud, TipoMaterial, puntitos

class solicitudadmin(admin.ModelAdmin):
    list_display = ('user', 'tipomat', 'fecha', 'estado', 'operario')
    list_filter = ('estado', 'operario')


admin.site.register(TipoMaterial)
admin.site.register(Solicitud)
admin.site.register(puntitos)