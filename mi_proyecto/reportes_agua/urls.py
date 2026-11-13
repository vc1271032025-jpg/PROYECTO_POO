from django.urls import path
from . import views

urlpatterns = [
    # 1. Página de inicio obligatoria del sistema
    path('inicio/', views.reporte_inicio, name='reporte_inicio'),
    
    # 2. Listado principal de reportes hídricos
    path('', views.reporte_listar, name='reporte_listar'),
    
    # 3. RUTA DE CREACIÓN (Ubicada arriba de forma estratégica para evitar colisiones)
    path('reporte/nuevo/', views.reporte_crear, name='reporte_crear'),
    
    # 4. Rutas dinámicas que dependen del ID del reporte (Primary Key)
    path('reporte/<int:pk>/', views.reporte_detalle, name='reporte_detalle'),
    path('reporte/<int:pk>/editar/', views.reporte_editar, name='reporte_editar'),
    path('reporte/<int:pk>/eliminar/', views.reporte_eliminar, name='reporte_eliminar'),
]

