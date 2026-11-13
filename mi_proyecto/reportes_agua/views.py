from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import ReporteAgua, Usuario, TipoIncidente, Ubicacion, Rol, Evidencia

def reporte_inicio(request):
    return render(request, 'reportes_agua/inicio.html')

def reporte_listar(request):
    try:
        reportes = ReporteAgua.objects.all().order_by('-fecha_registro')
    except Exception as e:
        reportes = []
        messages.warning(request, f"Aviso de base de datos: {e}")
    return render(request, 'reportes_agua/reporte_list.html', {'reportes': reportes})

def reporte_detalle(request, pk):
    reporte = get_object_or_404(ReporteAgua, pk=pk)
    return render(request, 'reportes_agua/reporte_detail.html', {'reporte': reporte})

def reporte_crear(request):
    if request.method == "POST":
        rol_base, _ = Rol.objects.get_or_create(id_rol=1, defaults={'nombre_rol': 'Administrador'})
        usuario_base, _ = Usuario.objects.get_or_create(
            id_usuario=1, 
            defaults={'nombre': 'Admin General', 'correo': 'admin@ecoagua.com', 'contrasena': 'root', 'id_rol': rol_base}
        )
        tipo_base, _ = TipoIncidente.objects.get_or_create(
            id_tipo_incidente=1, 
            defaults={'nombre_tipo': 'Fuga de Agua', 'descripcion': 'Ruptura de red distribución'}
        )

        direccion = request.POST.get('direccion_exacta', 'Dirección no especificada')
        municipio = request.POST.get('municipio', 'Municipio General')
        
        ultima_ubi = Ubicacion.objects.all().order_by('-id_ubicacion').first()
        nueva_ubi_id = (ultima_ubi.id_ubicacion + 1) if ultima_ubi else 1
        
        ubicacion_usuario = Ubicacion.objects.create(
            id_ubicacion=nueva_ubi_id,
            direccion_exacta=direccion,
            municipio=municipio
        )

        ultimo_reporte = ReporteAgua.objects.all().order_by('-id_reporte').first()
        nuevo_id = (ultimo_reporte.id_reporte + 1) if ultimo_reporte else 1

        fecha_actual = timezone.localtime(timezone.now())

        nuevo_reporte = ReporteAgua.objects.create(
            id_reporte=nuevo_id,
            fecha_registro=fecha_actual,
            descripcion=request.POST.get('descripcion'),
            prioridad=request.POST.get('prioridad', 'Media'),
            estado='Pendiente',
            id_usuario=usuario_base,
            id_tipo_incidente=tipo_base,
            id_ubicacion=ubicacion_usuario
        )

        imagen_adjunta = request.FILES.get('imagen')
        if imagen_adjunta:
            ultima_evidencia = Evidencia.objects.all().order_by('-id_evidencia').first()
            nueva_evidencia_id = (ultima_evidencia.id_evidencia + 1) if ultima_evidencia else 1
            
            Evidencia.objects.create(
                id_evidencia=nueva_evidencia_id,
                url_archivo=imagen_adjunta,
                fecha_subida=fecha_actual,
                id_reporte=nuevo_reporte
            )

        messages.success(request, "¡Incidente registrado físicamente con éxito!")
        return redirect('reporte_listar')
        
    return render(request, 'reportes_agua/reporte_form.html', {'reporte': None})

def reporte_editar(request, pk):
    reporte = get_object_or_404(ReporteAgua, pk=pk)
    if request.method == "POST":
        reporte.descripcion = request.POST.get('descripcion')
        reporte.prioridad = request.POST.get('prioridad')
        reporte.save()
        
        imagen_adjunta = request.FILES.get('imagen')
        if imagen_adjunta:
            ultima_evidencia = Evidencia.objects.all().order_by('-id_evidencia').first()
            nueva_evidencia_id = (ultima_evidencia.id_evidencia + 1) if ultima_evidencia else 1
            
            Evidencia.objects.create(
                id_evidencia=nueva_evidencia_id,
                url_archivo=imagen_adjunta,
                fecha_subida=timezone.localtime(timezone.now()),
                id_reporte=reporte
            )
            
        messages.info(request, "El reporte hídrico ha sido actualizado en la base de datos.")
        return redirect('reporte_listar')
    return render(request, 'reportes_agua/reporte_form.html', {'reporte': reporte})

def reporte_eliminar(request, pk):
    reporte = get_object_or_404(ReporteAgua, pk=pk)
    if request.method == "POST":
        reporte.delete()
        messages.error(request, "Registro eliminado permanentemente del servidor.")
        return redirect('reporte_listar')
    return render(request, 'reportes_agua/reporte_confirm_delete.html', {'reporte': reporte})
