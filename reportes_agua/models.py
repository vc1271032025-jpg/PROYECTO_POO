from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Ubicacion(models.Model):
    id_ubicacion = models.IntegerField(primary_key=True)
    direccion_exacta = models.CharField(max_length=255)
    municipio = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"{self.municipio} - {self.direccion_exacta}"

class ReporteAgua(models.Model):
    id_reporte = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, default='Pendiente')
    
 
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)
    ubicacion_fuga = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reporte #{self.id_reporte} - {self.estado}"

    def mostrar_detalle(self):
        return f"[{self.prioridad}] {self.descripcion} en {self.ubicacion_fuga}"
