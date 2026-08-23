"""
MODELO (MVC) — Contenido audiovisual destacado.
`fuente` admite una URL de YouTube (recomendado), un enlace directo .mp4
o una ruta relativa al proyecto. Vacío = aún sin video.
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
    fuente="https://pub-8bc5b19781954a6b82a08d838d66416e.r2.dev/Video%20Luis.mp4",
)
