"""
MODELO (MVC) — Datos de Preguntas Frecuentes.
Respuestas redactadas para personas sin conocimientos jurídicos.
Pendiente de validación final por el abogado.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PreguntaFrecuente:
    pregunta: str
    respuesta: str


PREGUNTAS_FRECUENTES: tuple[PreguntaFrecuente, ...] = (
    PreguntaFrecuente(
        pregunta="¿Toda consulta genera honorarios?",
        respuesta=(
            "Sí. Todas las consultas son servicios profesionales y generan "
            "honorarios. En la primera conversación le informamos el costo antes "
            "de iniciar, sin sorpresas ni cargos ocultos."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿Cómo se determinan los honorarios de mi caso?",
        respuesta=(
            "Dependen del tipo de proceso, su complejidad y el trabajo que "
            "requiere. Después de escuchar su caso se le presenta un presupuesto "
            "claro y por escrito antes de comenzar."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿Cómo agendo una consulta?",
        respuesta=(
            "La vía más rápida es el botón de WhatsApp de esta página. También "
            "puede dejar sus datos y será contactado para coordinar fecha y hora."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿Qué documentos debo tener listos para la consulta?",
        respuesta=(
            "Su documento de identidad y todo lo relacionado con su caso: "
            "notificaciones, citaciones, contratos, mensajes, correos, recibos o "
            "fotografías. Si no tiene algo, igual podemos orientarlo."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿En qué áreas del derecho se ofrece asesoría?",
        respuesta=(
            "La especialidad principal es el Derecho Penal: defensas, "
            "acompañamiento en investigaciones, denuncias y procesos ante los "
            "tribunales. Para otros temas se le indicará con honestidad si su "
            "caso puede atenderse o si requiere otro especialista."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿La información que comparta es confidencial?",
        respuesta=(
            "Totalmente. Todo lo que cuente está protegido por el secreto "
            "profesional abogado–cliente, incluso si decide no contratar el "
            "servicio después de la consulta."
        ),
    ),
)
