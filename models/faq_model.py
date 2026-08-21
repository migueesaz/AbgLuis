"""
MODELO (MVC) — Datos de Preguntas Frecuentes.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PreguntaFrecuente:
    pregunta: str
    respuesta: str


PREGUNTAS_FRECUENTES: tuple[PreguntaFrecuente, ...] = (
    PreguntaFrecuente(
        pregunta="¿Cómo agendo una consulta?",
        respuesta=(
            "Puede agendar a través del apartado de Contacto, por teléfono o "
            "correo electrónico. Confirmamos la cita en un plazo máximo de 24 horas."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿La primera consulta tiene costo?",
        respuesta=(
            "La primera consulta de valoración es sin costo. En ella evaluamos "
            "su caso y le informamos sobre las opciones y honorarios aplicables."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿Qué documentos debo llevar a la consulta?",
        respuesta=(
            "Documento de identidad, cualquier escrito o notificación relacionada "
            "con su caso, contratos firmados y pruebas disponibles (correos, "
            "recibos, fotografías)."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿Cuánto puede durar mi proceso?",
        respuesta=(
            "Depende del tipo de caso y de la carga del juzgado. Tras revisar su "
            "expediente le entregamos una hoja de ruta con plazos estimados y "
            "etapas del proceso."
        ),
    ),
    PreguntaFrecuente(
        pregunta="¿Mi información es confidencial?",
        respuesta=(
            "Sí. Toda la información que comparta está protegida por el secreto "
            "profesional abogado–cliente, incluso si decide no continuar con el "
            "servicio."
        ),
    ),
)
