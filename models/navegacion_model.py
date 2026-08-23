"""
MODELO (MVC) — Definición de las páginas de la aplicación.
Solo datos: ids, títulos e iconos de cada sección.
titulo vacío = pestaña solo con ícono (sin nombre).
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PaginaConfig:
    id: str
    icono: str
    titulo: str = ""


PAGINAS: tuple[PaginaConfig, ...] = (
    PaginaConfig(id="inicio", titulo="Inicio", icono="🏠"),
    PaginaConfig(id="trayectoria", titulo="Trayectoria", icono="🏛️"),
    PaginaConfig(id="faq", titulo="Preguntas Frecuentes", icono="❓"),
)


def pagina_por_id(id_pagina: str) -> PaginaConfig | None:
    return next((p for p in PAGINAS if p.id == id_pagina), None)


def pagina_inicial() -> PaginaConfig:
    return PAGINAS[0]
