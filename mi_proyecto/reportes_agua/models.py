import os
from django.db import models

USAR_NUBE = 'DATABASE_URL' in os.environ

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)

    class Meta:
        db_table = 'Rol'
        managed = USAR_NUBE

    def __str__(self):
        return self.nombre_rol


class TipoIncidente(models.Model):
    id_tipo_incidente = models.IntegerField(primary_key=True)
    nombre_tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'TipoIncidente'
        managed = USAR_NUBE

    def __str__(self):
        return self.nombre_tipo


class Ubicacion(models.Model):
    id_ubicacion = models.IntegerField(primary_key=True)
    direccion_exacta = models.CharField(max_length=255)
    municipio = models.CharField(max_length=100)

    class Meta:
        db_table = 'Ubicacion'
        managed = USAR_NUBE

    def __str__(self):
        return f"{self.municipio} - {self.direccion_exacta}"


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo = models.CharField(max_length=150)
    contrasena = models.CharField(max_length=150)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='id_rol')

    class Meta:
        db_table = 'Usuario'
        managed = USAR_NUBE

    def __str__(self):
        return self.nombre


class ReporteAgua(models.Model):
    id_reporte = models.IntegerField(primary_key=True)
    fecha_registro = models.DateTimeField()
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=50, default='Media')
    estado = models.CharField(max_length=50, default='Pendiente')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_tipo_incidente = models.ForeignKey(TipoIncidente, on_delete=models.CASCADE, db_column='id_tipo_incidente')
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, db_column='id_ubicacion')

    class Meta:
        db_table = 'ReporteAgua'
        managed = USAR_NUBE

    def __str__(self):
        return f"Reporte #{self.id_reporte} - {self.estado}"


class Evidencia(models.Model):
    id_evidencia = models.IntegerField(primary_key=True)
    url_archivo = models.ImageField(upload_to='evidencias/')
    fecha_subida = models.DateTimeField()
    id_reporte = models.ForeignKey(ReporteAgua, on_delete=models.CASCADE, db_column='id_reporte', related_name='evidencias')

    class Meta:
        db_table = 'Evidencia'
        managed = USAR_NUBE

    def __str__(self):
        return f"Evidencia #{self.id_evidencia}"
