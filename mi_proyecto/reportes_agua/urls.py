from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.reporte_inicio, name='reporte_inicio'),
    path('', views.reporte_listar, name='reporte_listar'),
    path('reporte/nuevo/', views.reporte_crear, name='reporte_crear'),
    path('reporte/<int:pk>/', views.reporte_detalle, name='reporte_detalle'),
    path('reporte/<int:pk>/editar/', views.reporte_editar, name='reporte_editar'),
    path('reporte/<int:pk>/eliminar/', views.reporte_eliminar, name='reporte_eliminar'),
]

