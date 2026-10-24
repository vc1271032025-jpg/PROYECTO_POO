from django.contrib import admin

from django.contrib import admin
from .models import Ubicacion, ReporteAgua

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_ubicacion', 'municipio', 'direccion_exacta')

@admin.register(ReporteAgua)
class ReporteAguaAdmin(admin.ModelAdmin):
    list_display = ('id_reporte', 'prioridad', 'estado', 'usuario_creador')
    list_filter = ('estado', 'prioridad')
