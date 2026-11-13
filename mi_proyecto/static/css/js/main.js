/* ==========================================================================
   INTERACTIVIDAD BÁSICA DEL SISTEMA ECOAGUA (JAVASCRIPT)
   - Filtro de búsqueda en tiempo real (Listado)
   - Validación interactiva de campos del formulario antes del envío
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
    
    // 1. CONTROL DEL FILTRO DE BÚSQUEDA DINÁMICA (Para reporte_list.html)
    const buscador = document.getElementById("inputBuscador");
    if (buscador) {
        buscador.addEventListener("keyup", function (e) {
            const textoBusqueda = e.target.value.toLowerCase();
            const tarjetas = document.querySelectorAll(".contenedor-tarjeta");

            tarjetas.forEach(tarjeta => {
                // Captura el contenido del párrafo descriptivo dentro de cada tarjeta
                const descripcion = tarjeta.querySelector(".card-text").textContent.toLowerCase();
                
                // Muestra u oculta la tarjeta usando clases de Bootstrap sin recargar la página
                if (descripcion.includes(textoBusqueda)) {
                    tarjeta.style.display = "block";
                } else {
                    tarjeta.style.display = "none";
                }
            });
        });
    }

    // 2. VALIDACIÓN INTERACTIVA DE FORMULARIOS (Para reporte_form.html)
    const formulario = document.getElementById("formReporte");
    if (formulario) {
        formulario.addEventListener("submit", function (e) {
            const textareaDesc = document.getElementById("id_descripcion");
            
            // Regla: Bloquea descripciones genéricas cortas que alteren las auditorías
            if (textareaDesc && textareaDesc.value.trim().length < 10) {
                e.preventDefault(); // Detiene el envío hacia SQL Server
                alert("⚠️ Error técnico: La descripción del incidente debe ser más detallada (mínimo 10 caracteres).");
                textareaDesc.classList.add("is-invalid"); // Marca el input en rojo con Bootstrap
            }
        });
    }
});
