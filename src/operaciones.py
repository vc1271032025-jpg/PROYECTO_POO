
from modelos import Usuario, Ubicacion, ReporteAgua 


def registrar_nuevo_incidente_comunitario():
    print("--- INICIANDO REGISTRO DE ALERTA DE AGUA ---")
    
   
    vecino = Usuario(id_usuario=1, nombre="Carlos Méndez", correo="carlos@email.com", contrasena="12345")
    
  
    ubicacion_fuga = Ubicacion(
        id_ubicacion=101, 
        direccion_exacta="Calle Principal, frente a la escuela", 
        municipio="Ojos de Agua", 
        latitud=14.1234, 
        longitud=-89.1234
    )
    
    
    nuevo_reporte = ReporteAgua(
        id_reporte=5001,
        descripcion="Tubería rota desperdiciando agua limpia desde hace 2 días.",
        prioridad="Alta",
        estado="Pendiente",
        usuario_creador=vecino,
        ubicacion_fuga=ubicacion_fuga
    )
    
    
    print("\n--- DETALLE DEL REPORTE GUARDADO ---")
    nuevo_reporte.mostrar_detalle()


registrar_nuevo_incidente_comunitario()

