Integrantes
Cristhofer Santos Portillo Landaverde
Cristian Ariel Valle Claros
Bryan Alejandro Alas Delgado
Orlando Samael Menjivar Bonilla

Descripción inicial de la problemática

¿Qué problema ambiental desean atender?
Se busca atender la pérdida de recursos hídricos ocasionada por fugas y tuberías dañadas, el desperdicio de agua y los casos de contaminación hídrica.

¿Dónde ocurre o podría investigarse?
Esta problemática ocurre a nivel local, específicamente dentro de las comunidades y centros educativos. La aplicación permitirá indicar la ubicación exacta de los incidentes y filtrar los reportes por zona.

¿Por qué consideran importante atenderlo? 
Porque la falta de documentación actual impide gestionar los incidentes adecuadamente. Resolverlo mediante este sistema permitirá documentar casos con evidencias fotográficas, asignar niveles de prioridad, registrar acciones de seguimiento y actualizar el estado de cada reporte para solucionarlo.

¿Quiénes resultan afectados por esta problemática?
Principalmente las comunidades, centros educativos, juntas de agua, alcaldías y las asociaciones comunitarias.

Parte 2:

Descripción de la situación encontrada

Hemos identificado que en la comunidad se enfrentan deficiencias constantes en la gestión y conservación de los recursos hídricos. A diario se presentan fugas en redes de distribución, tuberías deterioradas, actos de desperdicio de agua y focos de contaminación que ponen en riesgo la salud pública y la disponibilidad del servicio.

Sin embargo, el hallazgo más crítico identificado en el entorno local es la falta sistemática de registros y mecanismos centralizados para documentar, priorizar y dar seguimiento a este tipo de incidentes. Cuando un ciudadano detecta una fuga o un problema de contaminación, la información suele quedarse en reportes verbales e informales que no llegan oportunamente a las autoridades correspondientes (juntas de agua o alcaldías). Esto genera una falta de visibilidad del estado real de la infraestructura hídrica comunitaria y perpetúa la ineficiencia en las labores de reparación y respuesta.

Personas o grupos afectados

La problemática impacta directamente a los habitantes de la comunidad, a la población estudiantes y docentes de centros educativos, así como a las juntas de agua, alcaldías y asociaciones comunitarias, cuya labor operativa se ve sobrepasada al no contar con información fidedigna ni organizada.

Requisitos funcionales

-Registrar incidentes de agua

-Seleccionar tipo de problema

-Indicar ubicación y fecha

-Adjuntar fotografía de evidencia

-Asignar nivel de prioridad

-Registrar acciones de seguimiento

-Actualizar el estado del caso

-Filtrar y consultar reportes


Requisitos no funcionales

-Restricción Tecnológica
La aplicación web de monitoreo hídrico deberá ser desarrollada utilizando el lenguaje de programación Python bajo el framework Django, implementando sus componentes nativos mediante programación orientada a objetos (POO).

-Sistema de Gestión de Base de Datos (Persistencia)

El almacenamiento, integridad y persistencia de todos los datos transaccionales, usuarios y registros de incidentes se gestionará obligatoriamente mediante una base de datos SQL Server.

-Adaptabilidad de la Interfaz 

La interfaz gráfica de usuario deberá ser completamente adaptable (Responsive Design), garantizando que las pantallas de visualización de datos y los formularios de reporte operen correctamente tanto en computadoras de escritorio como en dispositivos móviles.

-Validación Estricta de Formularios
Todos los formularios de captura del sistema deberán implementar validaciones rigurosas en el cliente y en el servidor, impidiendo el envío de datos si existen campos obligatorios vacíos o si los formatos de imagen adjuntos no son válidos.

-Seguridad y Protección de Datos
El sistema deberá proteger la información personal de los miembros de la comunidad que registran las denuncias mediante el uso de tokens anti-CSRF nativos de Django y mecanismos que aseguren el anonimato de los datos sensibles en las consultas públicas.



Actualizacion semana 3

3. Identificación de las clases


Clase: Usuario

Responsabilidad: Representar a las personas que interactúan con el sistema, ya sean miembros de la comunidad, estudiantes voluntarios o administradores.


Atributos: IdUsuario, Nombre, Correo, Contraseña.


Métodos: iniciar_sesion(), consultar_reportes(), registrar_incidente().


Relación: Se relaciona con la clase ReporteAgua (un usuario crea uno o muchos reportes).


Clase: ReporteAgua

Responsabilidad: Centralizar y gestionar la información de los incidentes de fugas, desperdicio o contaminación hídrica documentados en la comunidad.


Atributos: IdReporte, FechaRegistro, Descripción, Prioridad, Estado.


Métodos: crear_reporte(), asignar_prioridad(), actualizar_estado(), mostrar_detalle().


Relación: Se relaciona de forma directa con Usuario, TipoIncidente, Ubicacion, Seguimiento y Evidencia.


Clase: Ubicacion

Responsabilidad: Almacenar de forma precisa las coordenadas geográficas y la dirección donde ocurre cada problema hídrico.


Atributos: IdUbicacion, DireccionExacta, Municipio, Latitud, Longitud.


Métodos: registrar_coordenadas(), obtener_direccion().


Relación: Pertenece a la clase ReporteAgua (cada reporte tiene asociada una única ubicación).


Clase: Seguimiento

Responsabilidad: Documentar el historial de actividades técnicas, reparaciones y cambios de estado que se aplican a un caso particular a lo largo del tiempo.


Atributos: IdSeguimiento, EstadoAnterior, NuevoEstado, FechaActualizacion, Comentario.


Métodos: registrar_avance(), consultar_historial().


Relación: Se asocia a un ReporteAgua y es generado por un Usuario (usualmente administradores o voluntarios).


4. Aplicación de Programación Orientada a Objetos


Clases: Funcionan como los moldes o plantillas principales (ej. ReporteAgua, Usuario, Evidencia) que definen la estructura de datos que se guardará en la base de datos SQL Server mediante el framework Django.


Objetos: Son las instancias reales y concretas que se crean a partir de las clases. Por ejemplo, un objeto de ReporteAgua sería una alerta específica sobre una "Fuga de agua en el Bº Las Flores" creada hoy y en estado Pendiente.


Atributos: Son las propiedades o datos específicos de cada entidad, como la Latitud y Longitud para la ubicación, o el Estado y la Prioridad para controlar el nivel de emergencia operativa de los reportes.


Métodos: Son las acciones o funciones que dan cumplimiento a los requisitos funcionales, tales como asignar_nivel_prioridad() o modificar_estado_caso().


Encapsulamiento: Se aplica para proteger los datos sensibles (como ocultar las contraseñas del Usuario) y garantizar que el estado de un reporte solo cambie utilizando un método válido (por ejemplo, pasando por una validación estricta de formulario) en lugar de modificarse directamente.


Herencia: El sistema cuenta con tres tipos de perfiles definidos. Se puede tener una clase base abstracta llamada Usuario de la cual hereden clases específicas como Administrador, MiembroComunidad y EstudianteVoluntario. Esto permite que todos compartan atributos comunes (nombre, correo) pero que el Administrador tenga capacidades exclusivas heredadas, como asignar prioridades globales.


Polimorfismo: Apoyándose en la herencia, un método genérico como consultar_informacion() actuará diferente según el usuario. Si lo ejecuta un Administrador, desplegará un panel global de métricas con filtros avanzados; si lo ejecuta un MiembroComunidad, solo mostrará los reportes públicos cercanos y el estado de sus propios casos.


Abstracción: Se utiliza para ocultar la complejidad interna del sistema al ciudadano. Cuando un vecino reporta una fuga, interactúa con un formulario intuitivo donde solo selecciona opciones de un menú y sube una foto, ignorando toda la lógica de tokens anti-CSRF y la escritura relacional en SQL Server que el sistema ejecuta por detrás.


Relaciones entre clases: Se establecen para conectar la información y modelar la realidad, como se refleja en el modelo de base de datos. Una relación clave es de uno a muchos: un Usuario puede generar múltiples Reportes Agua, y un ReporteAgua puede poseer múltiples imágenes en la clase Evidencia y múltiples registros en la clase Seguimiento.

   9.Organización del desarrollo

Integrantes                             Rol
Cristhofer Santos Portillo Landaverde  Analizis                 organizacion semnal
Bryan Alejandro Alas Delgado           Diseño de base de datos  Aplicacion de conceptos poo
Orlando Samael Menjívar Bonilla        Arquitectura y datos     Diagrama
Bayron Alberto López Zamora            Analizis tecnico         Direccionamiento de datos
Cristian Ariel Valle Claros            Documentacion            organizacion del proyecto

