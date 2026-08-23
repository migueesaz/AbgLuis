"""
MODELO (MVC) — Datos de la trayectoria profesional.
Estructura por bloques (formación, experiencia, cargos, especializaciones,
reconocimientos). Los valores actuales son PLACEHOLDERS pendientes de
sustituir por información autorizada.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class EtapaTrayectoria:
    periodo: str
    titulo: str
    detalle: str = ""


@dataclass(frozen=True)
class BloqueTrayectoria:
    id: str
    titulo: str
    icono: str
    etapas: tuple[EtapaTrayectoria, ...]


TRAYECTORIA: tuple[BloqueTrayectoria, ...] = (
    BloqueTrayectoria(
        id="formacion",
        titulo="Formación Académica",
        icono="🎓",
        etapas=(
            EtapaTrayectoria("[Por definir]", "[Título universitario]", "[Institución y año]"),
            EtapaTrayectoria("[Por definir]", "[Estudios de especialización]", "[Institución y año]"),
        ),
    ),
    BloqueTrayectoria(
        id="experiencia",
        titulo="Experiencia Profesional",
        icono="💼",
        etapas=(
            EtapaTrayectoria("[Por definir]", "[Cargo o puesto]", "[Descripción breve]"),
            EtapaTrayectoria("[Por definir]", "[Cargo o puesto]", "[Descripción breve]"),
        ),
    ),
    BloqueTrayectoria(
        id="cargos",
        titulo="Cargos Desempeñados",
        icono="🏅",
        etapas=(
            EtapaTrayectoria("[Por definir]", "Fiscal del Ministerio Público", "[Detalles del cargo]"),
        ),
    ),
    BloqueTrayectoria(
        id="especializaciones",
        titulo="Especializaciones",
        icono="⚖️",
        etapas=(
            EtapaTrayectoria("", "[Área de especialización]"),
            EtapaTrayectoria("", "[Área de especialización]"),
        ),
    ),
    BloqueTrayectoria(
        id="reconocimientos",
        titulo="Reconocimientos y Logros",
        icono="🏆",
        etapas=(
            EtapaTrayectoria("[Por definir]", "[Reconocimiento obtenido]", "[Entidad otorgante]"),
        ),
    ),
)
