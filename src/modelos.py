
from datetime import datetime

class Ubicacion:
   
    def __init__(self, id_ubicacion, direccion_exacta, municipio, latitud, longitud):
        self.id_ubicacion = id_ubicacion
        self.direccion_exacta = direccion_exacta
        self.municipio = municipio
        self.latitud = latitud
        self.longitud = longitud

    
    def obtener_direccion(self):
        return f"{self.direccion_exacta}, {self.municipio} (Lat: {self.latitud}, Lon: {self.longitud})"

    def registrar_coordenadas(self, nueva_lat, nueva_lon):
        self.latitud = nueva_lat
        self.longitud = nueva_lon

class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self._contrasena = contrasena 

    def iniciar_sesion(self, correo_ingresado, contrasena_ingresada):
        return self.correo == correo_ingresado and self._contrasena == contrasena_ingresada

class ReporteAgua:
    def __init__(self, id_reporte, descripcion, prioridad, estado, usuario_creador, ubicacion_fuga):
        self.id_reporte = id_reporte
        self.fecha_registro = datetime.now()
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
       
        self.usuario = usuario_creador 
        self.ubicacion = ubicacion_fuga 

    def mostrar_detalle(self):
        print(f"Reporte #{self.id_reporte} - {self.estado}")
        print(f"Descripción: {self.descripcion}")
        print(f"Ubicación: {self.ubicacion.obtener_direccion()}")
        print(f"Prioridad: {self.prioridad}")

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado del reporte se actualizó a: {self.estado}")

