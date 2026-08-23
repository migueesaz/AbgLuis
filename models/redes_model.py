"""
MODELO (MVC) — Redes sociales oficiales del abogado.
Solo datos: nombre y URL de cada perfil. Sustituir las URLs de ejemplo
por los perfiles definitivos.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class RedSocial:
    nombre: str
    url: str


REDES_SOCIALES: tuple[RedSocial, ...] = (
    RedSocial(
        nombre="Instagram",
        url="https://www.instagram.com/sanchezluis1975",
    ),
    RedSocial(
        nombre="TikTok",
        url="https://www.tiktok.com/@luis_sanchez_1975",
    ),
)
