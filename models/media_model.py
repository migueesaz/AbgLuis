"""
MODELO (MVC) — Contenido audiovisual destacado.
`fuente` admite:
  - "static/archivo.mp4": servido por Streamlit desde ./static (recomendado).
  - URL de YouTube o enlace directo (.mp4).
Vacío = aún sin video.
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
    fuente="static/video_luis.mp4",
)
