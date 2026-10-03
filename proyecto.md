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
