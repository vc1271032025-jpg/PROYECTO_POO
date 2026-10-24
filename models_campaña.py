from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CampañaAmbiental(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Campaña")
    descripcion = models.TextField(verbose_name="Descripción de Objetivos")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalización")
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Presupuesto ($)")
    # Relación ManyToMany: Múltiples usuarios participan en múltiples campañas
    voluntarios = models.ManyToManyField(User, related_name='campanas_inscritas', blank=True)

    class Meta:
        verbose_name_plural = "Campañas Ambientales"

    def __str__(self):
        return self.nombre

    def esta_activa(self):
        """Método propio: Evalúa la vigencia temporal de la campaña."""
        hoy = timezone.now().date()
        return self.fecha_inicio <= hoy <= self.fecha_fin
