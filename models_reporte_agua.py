from django.db import models
from django.contrib.auth.models import User

class ReporteAgua(models.Model):
    registrado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reportes_agua')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    consumo_litros = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Consumo (Litros)")
    calidad_optima = models.BooleanField(default=True, verbose_name="¿Calidad Óptima?")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones Técnicas")

    class Meta:
        verbose_name_plural = "Reportes de Agua"

    def __str__(self):
        return f"Reporte #{self.id} - {self.fecha_registro.strftime('%d/%m/%Y')}"

    def requiere_inspeccion_urgente(self):
        """Método propio: Evalúa si el reporte necesita atención inmediata."""
        return not self.calidad_optima or self.consumo_litros > 50000
