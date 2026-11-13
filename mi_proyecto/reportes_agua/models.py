from django.db import models

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, db_column='IdRol')
    nombre_rol = models.CharField(max_length=100, db_column='NombreRol')
    descripcion = models.CharField(max_length=255, db_column='Descripción', blank=True, null=True)

    class Meta:
        db_table = 'Rol'
        managed = False

    def __str__(self):
        return self.nombre_rol


class TipoIncidente(models.Model):
    id_tipo_incidente = models.IntegerField(primary_key=True, db_column='IdTipoIncidente')
    nombre_tipo = models.CharField(max_length=100, db_column='NombreTipo')
    descripcion = models.CharField(max_length=255, db_column='Descripción', blank=True, null=True)

    class Meta:
        db_table = 'TipoIncidente'
        managed = False

    def __str__(self):
        return self.nombre_tipo


class Ubicacion(models.Model):
    id_ubicacion = models.IntegerField(primary_key=True, db_column='IdUbicacion')
    direccion_exacta = models.CharField(max_length=255, db_column='DireccionExacta')
    municipio = models.CharField(max_length=100, db_column='Municipio')
    latitud = models.DecimalField(max_digits=10, decimal_places=8, db_column='Latitud', blank=True, null=True)
    longitud = models.DecimalField(max_digits=11, decimal_places=8, db_column='Longitud', blank=True, null=True)

    class Meta:
        db_table = 'Ubicacion'
        managed = False

    def __str__(self):
        return f"{self.municipio} - {self.direccion_exacta[:30]}"


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, db_column='IdUsuario')
    nombre = models.CharField(max_length=150, db_column='Nombre')
    correo = models.CharField(max_length=150, unique=True, db_column='Correo')
    contrasena = models.CharField(max_length=255, db_column='Contraseña')
    id_rol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='IdRol')

    class Meta:
        db_table = 'Usuario'
        managed = False

    def __str__(self):
        return self.nombre


class ReporteAgua(models.Model):
    id_reporte = models.IntegerField(primary_key=True, db_column='IdReporte')
    fecha_registro = models.DateTimeField(db_column='FechaRegistro')
    descripcion = models.CharField(max_length=500, db_column='Descripción', blank=True, null=True)
    prioridad = models.CharField(max_length=50, db_column='Prioridad', blank=True, null=True)
    estado = models.CharField(max_length=50, db_column='Estado', default='Pendiente')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='IdUsuario')
    id_tipo_incidente = models.ForeignKey(TipoIncidente, on_delete=models.PROTECT, db_column='IdTipoIncidente')
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT, db_column='IdUbicacion')

    class Meta:
        db_table = 'ReporteAgua'
        managed = False

    def __str__(self):
        return f"Reporte #{self.id_reporte} - {self.estado}"




class Evidencia(models.Model):
    id_evidencia = models.IntegerField(primary_key=True, db_column='IdEvidencia')
    url_archivo = models.ImageField(upload_to='evidencias/', db_column='UrlArchivo') # Maneja la carga de archivos
    fecha_subida = models.DateTimeField(db_column='FechaSubida', auto_now_add=True)
    id_reporte = models.ForeignKey('ReporteAgua', on_delete=models.CASCADE, db_column='IdReporte', related_name='evidencias')

    class Meta:
        db_table = 'Evidencia'
        managed = False # Respeta tu script original de base de datos
