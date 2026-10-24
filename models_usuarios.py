from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre del Rol")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre

    def obtener_resumen(self):
        """Método propio: Retorna descripción corta."""
        return f"{self.nombre}: {self.descripcion[:30]}..." if self.descripcion else self.nombre

class Perfil(models.Model):
    # Relación uno a uno con el usuario nativo de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")

    class Meta:
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

    def es_administrador(self):
        """Método propio: Lógica de negocio para validar el rol."""
        return self.rol.nombre.lower() == 'administrador' if self.rol else False
