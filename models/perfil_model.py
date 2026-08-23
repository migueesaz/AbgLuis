"""
MODELO (MVC) — Datos del perfil profesional mostrado en la cabecera.
"""
from dataclasses import dataclass
from urllib.parse import quote


@dataclass(frozen=True)
class Perfil:
    nombre: str
    titulo: str
    foto_ruta: str  # relativa a la raíz del proyecto
    marca: str = "LEX"
    descripcion: str = ""  # párrafo de presentación profesional
    whatsapp_numero: str = ""  # solo dígitos, con código de país
    whatsapp_mensaje: str = "Hola, me gustaría agendar una consulta."


PERFIL = Perfil(
    nombre="Luis Eduardo Sanchez Camargo",
    titulo="Especialista en Derecho Penal y Procesal Penal | Fiscal Jubilado del Ministerio Público",
    foto_ruta="assets/foto_perfil.jpg",
    descripcion=(
        "[PLACEHOLDER — Descripción profesional pendiente de aprobación] "
        "Abogado especialista en Derecho Penal con experiencia como Fiscal del "
        "Ministerio Público. Acompaño a mis clientes en cada etapa del proceso "
        "penal con rigor técnico, estrategia clara y compromiso absoluto con su defensa."
    ),
    whatsapp_numero="584149027746",
)

_ENLACE_WHATSAPP = (
    f"https://wa.me/{PERFIL.whatsapp_numero}"
    f"?text={quote(PERFIL.whatsapp_mensaje)}"
)


def enlace_whatsapp() -> str:
    """Devuelve el enlace directo (wa.me) con mensaje predefinido."""
    return _ENLACE_WHATSAPP
