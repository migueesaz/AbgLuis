# ⚖️ LEX — Portafolio Profesional Jurídico de Luis Eduardo Sanchez Camargo

> Portafolio profesional jurídico desarrollado con Python y Streamlit.

---

# 📋 Plan de desarrollo

Este documento funciona como una hoja de ruta para el desarrollo de **LEX**.

La idea es ir completando cada apartado progresivamente y marcarlo como realizado cuando esté terminado.

---

# 🟢 1. Base actual del proyecto

- [x] Crear estructura inicial del proyecto.
- [x] Implementar aplicación principal con Streamlit.
- [x] Organizar el proyecto utilizando una estructura MVC.
- [x] Separar modelos, vistas y controladores.
- [x] Crear sistema de navegación mediante pestañas.
- [x] Configurar estilos CSS independientes.
- [x] Crear estructura de componentes reutilizables.
- [x] Configurar `requirements.txt`.
- [x] Configurar `.streamlit`.
- [x] Incorporar fotografía profesional.
- [x] Crear presentación inicial del abogado.
- [x] Crear sección de Biblioteca de Éxitos.
- [x] Crear sección de Preguntas Frecuentes.
- [x] Crear footer de la página.
- [x] Crear estructura para futuras secciones.

---

# 🟡 2. Mejorar la página principal

- [x] Diseñar una presentación principal más completa.
- [x] Incorporar una descripción profesional del abogado. *(PLACEHOLDER pendiente de aprobación en `models/perfil_model.py`)*
- [x] Añadir una llamada a la acción para contactar.
- [x] Preparar espacio para el botón de WhatsApp.
- [x] Mejorar la distribución visual de la página.
- [ ] Revisar la experiencia del usuario al entrar al sitio.
- [x] Revisar la adaptación a diferentes tamaños de pantalla.

---

# 🟡 3. Sección "Trayectoria"

Crear una sección dedicada exclusivamente a mostrar la trayectoria profesional del abogado.

## Información

> Los campos se encuentran como placeholders en `models/trayectoria_model.py`, listos para rellenar.

- [ ] Definir información profesional que será publicada.
- [ ] Agregar formación académica.
- [ ] Agregar experiencia profesional.
- [ ] Agregar cargos desempeñados.
- [ ] Agregar especializaciones.
- [ ] Agregar reconocimientos o logros.
- [ ] Revisar qué información puede hacerse pública.

## Diseño

- [x] Diseñar la sección visualmente.
- [x] Crear estructura para presentar la trayectoria. *(bloques por categoría)*
- [x] Evaluar implementación como línea de tiempo. *(implementada)*
- [x] Crear componentes reutilizables para cada etapa.
- [x] Integrar la sección con la navegación principal.

---

# 🟡 4. Contacto mediante WhatsApp

Implementar WhatsApp como principal medio de contacto entre el visitante y el abogado.

- [x] Obtener el número de WhatsApp que será utilizado. (+58 412 9072234, en `models/perfil_model.py`)
- [x] Crear enlace directo de WhatsApp.
- [x] Crear botón de contacto.
- [x] Integrar el botón en la página principal.
- [x] Evaluar ubicación del botón dentro del sitio.
- [x] Agregar una llamada a la acción.
- [x] Probar el enlace desde computadora.
- [x] Probar el enlace desde dispositivo móvil.
- [x] Verificar que el enlace abra correctamente WhatsApp.
- [x] Revisar el diseño del botón.

---

# 🟡 5. Biblioteca de Éxitos

La Biblioteca de Éxitos actualmente utiliza información demostrativa.

## Mejoras

- [ ] Definir qué información podrá mostrarse públicamente.
- [ ] Sustituir progresivamente los datos ficticios cuando exista información autorizada.
- [ ] Revisar la estructura de cada caso.
- [ ] Mejorar las tarjetas visuales.
- [ ] Evaluar filtros por área jurídica.
- [ ] Evaluar filtros por año.
- [ ] Evaluar una vista detallada para cada caso.
- [ ] Implementar medidas para proteger información confidencial.

> ⚠️ No publicar información de clientes o casos reales sin autorización y sin considerar las obligaciones de confidencialidad correspondientes.

---

# 🟡 6. Preguntas frecuentes

- [x] Crear sección de preguntas frecuentes.
- [x] Crear preguntas desplegables.
- [x] Revisar el contenido actual. *(alineado al servicio: honorarios por consulta, contacto por WhatsApp, enfoque penal)*
- [ ] Validar las respuestas con el abogado.
- [x] Agregar preguntas adicionales.
- [ ] Organizar las preguntas por categorías.
- [x] Revisar que la información sea clara para personas que no tengan conocimientos jurídicos.

---

# 🟠 7. Contenido audiovisual

Preparar LEX para convertirse también en una plataforma de contenido jurídico.

## 🎙️ Podcast

- [ ] Definir dónde se alojarán los episodios.
- [ ] Definir formato de publicación.
- [ ] Crear sección de podcast.
- [ ] Diseñar tarjetas para episodios.
- [ ] Incorporar miniaturas.
- [ ] Incorporar título y descripción.
- [ ] Añadir enlaces a los episodios.
- [ ] Evaluar integración de videos.

## 📱 Videos cortos

Crear un espacio para contenido de formato corto.

- [ ] Definir plataforma principal.
- [ ] Evaluar TikTok.
- [ ] Evaluar Instagram Reels.
- [ ] Evaluar YouTube Shorts.
- [ ] Crear sección de videos cortos.
- [ ] Diseñar presentación de los videos.
- [ ] Incorporar enlaces a las plataformas correspondientes.

## 🎥 Videos promocionales

- [ ] Crear video de presentación profesional.
- [x] Crear espacio para video principal. *(reel alojado en Cloudflare R2, en bucle; fuente en `models/media_model.py`)*
- [ ] Preparar sección de contenido promocional.
- [ ] Incorporar videos relacionados con la práctica profesional.

---

# 🟠 8. Redes sociales

Preparar la estructura para conectar LEX con las redes profesionales del abogado.

- [x] Definir redes sociales oficiales. *(Instagram: @sanchezluis1975 · TikTok: @luis_sanchez_1975)*
- [x] Crear sección o botones de redes sociales.
- [x] Agregar enlaces oficiales.
- [ ] Revisar diseño de los iconos.
- [ ] Integrar redes sociales con el contenido multimedia.

---

# 🟠 9. Formulario de contacto

> Esta funcionalidad queda planificada para una etapa posterior.

- [ ] Diseñar formulario.
- [ ] Definir información que solicitará.
- [ ] Nombre.
- [ ] Correo electrónico.
- [ ] Teléfono.
- [ ] Motivo de contacto.
- [ ] Mensaje.
- [ ] Validar campos.
- [ ] Definir dónde se recibirán las solicitudes.
- [ ] Implementar sistema de envío.
- [ ] Añadir medidas de seguridad.
- [ ] Añadir aviso de privacidad.
- [ ] Probar funcionamiento.

---

# 🔵 10. Posible sistema de citas

Funcionalidad futura.

- [ ] Analizar si realmente es necesaria.
- [ ] Definir disponibilidad del abogado.
- [ ] Definir tipos de consulta.
- [ ] Diseñar sistema de solicitud.
- [ ] Evaluar integración con calendario.
- [ ] Definir mecanismo de confirmación.
- [ ] Evaluar automatización.

---

# 🔵 11. Mejoras visuales

- [ ] Definir identidad visual definitiva de LEX.
- [ ] Definir paleta de colores.
- [ ] Revisar tipografías.
- [ ] Crear logo de LEX.
- [ ] Mejorar transiciones visuales.
- [ ] Revisar espaciado.
- [ ] Revisar tamaños de elementos.
- [ ] Mejorar tarjetas.
- [ ] Mejorar botones.
- [ ] Mejorar navegación.
- [ ] Revisar versión móvil.
- [ ] Revisar accesibilidad.

---

# 🔵 12. Experiencia del usuario

- [ ] Revisar navegación completa.
- [ ] Reducir pasos innecesarios.
- [ ] Crear llamadas a la acción claras.
- [ ] Facilitar el acceso al contacto.
- [ ] Facilitar el acceso a la trayectoria.
- [ ] Facilitar el acceso al contenido.
- [ ] Revisar tiempos de carga.
- [ ] Revisar comportamiento en dispositivos móviles.

---

# 🔵 13. Seguridad y privacidad

Debido a que LEX pertenece al ámbito jurídico, la privacidad debe ser una prioridad.

- [ ] Revisar información personal publicada.
- [ ] Revisar información profesional publicada.
- [ ] Revisar información de casos.
- [ ] Evitar publicar información confidencial.
- [ ] Revisar enlaces externos.
- [ ] Revisar datos utilizados en formularios futuros.
- [ ] Crear aviso de privacidad si se implementa un formulario.
- [ ] Revisar manejo de datos personales.
- [ ] Revisar credenciales y secretos antes de publicar el proyecto.

---

# 🟣 14. Preparación para producción

Antes de publicar LEX:

- [ ] Eliminar archivos innecesarios.
- [ ] No incluir `venv` en el repositorio.
- [ ] Crear `.gitignore`.
- [ ] Revisar archivos temporales.
- [ ] Revisar archivos de configuración.
- [ ] Revisar dependencias.
- [ ] Probar instalación desde cero.
- [ ] Probar la aplicación sin el entorno de desarrollo original.
- [ ] Revisar errores.
- [ ] Revisar consola.
- [ ] Optimizar recursos.
- [ ] Preparar versión de producción.

---

# 🟣 15. Publicación

Cuando el proyecto esté listo:

- [ ] Crear repositorio definitivo.
- [ ] Preparar README definitivo.
- [ ] Configurar repositorio.
- [ ] Configurar `.gitignore`.
- [ ] Subir proyecto.
- [ ] Elegir plataforma de despliegue.
- [ ] Configurar variables necesarias.
- [ ] Realizar despliegue.
- [ ] Probar versión online.
- [ ] Corregir errores de producción.
- [ ] Crear dominio personalizado si se considera necesario.

---

# 📝 16. Documentación final

Cuando el proyecto esté más avanzado:

- [ ] Actualizar descripción del proyecto.
- [ ] Actualizar funcionalidades.
- [ ] Actualizar tecnologías.
- [ ] Actualizar estructura del proyecto.
- [ ] Añadir capturas de pantalla.
- [ ] Documentar instalación.
- [ ] Documentar ejecución.
- [ ] Documentar arquitectura.
- [ ] Documentar funcionalidades.
- [ ] Documentar futuras mejoras.
- [ ] Añadir información del autor.
- [ ] Definir licencia.

---

# 🚀 Visión futura de LEX

La visión de LEX es evolucionar desde un portafolio profesional hacia una plataforma digital jurídica más completa.

La evolución prevista es:

```text
                    LEX
                     │
          Portafolio Profesional
                     │
       ┌─────────────┼─────────────┐
       │             │             │
    Perfil       Trayectoria    Éxitos
       │             │             │
       └─────────────┼─────────────┘
                     │
                  Contacto
                     │
                  WhatsApp
                     │
          ┌──────────┼──────────┐
          │          │          │
       Podcast    Videos     Redes
          │       cortos       │
          │          │          │
          └──────────┼──────────┘
                     │
              Formulario
                     │
                Citas futuras