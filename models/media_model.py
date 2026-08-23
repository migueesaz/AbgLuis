"""
MODELO (MVC) — Contenido audiovisual destacado.
`fuente` admite una ruta relativa al proyecto (p. ej. assets/video.mp4)
o una URL (YouTube o enlace directo .mp4). Vacío = aún sin video.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class VideoConfig:
    titulo: str
    descripcion: str = ""
    fuente: str = ""


VIDEO_PRINCIPAL = VideoConfig(
    titulo="Conoce mi práctica",
    descripcion="Un vistazo a mi experiencia y a mi forma de trabajar.",
    fuente="templates/Video Luis.mp4",
)
