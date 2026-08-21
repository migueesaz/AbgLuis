"""
CONTROLADOR (MVC) — Orquesta modelos y vistas.
Las páginas se muestran en pestañas superiores (st.tabs).
"""
from models.footer_model import FooterConfig
from models.navegacion_model import PAGINAS
from views.components.footer_view import render_footer
from views.components.tabs_view import render_tabs
from views.pages.exitos_view import render_exitos
from views.pages.faq_view import render_faq
from views.pages.generic_view import render_generic
from views.pages.inicio_view import render_inicio

_RUTA_VISTAS = {
    "inicio": render_inicio,
    "exitos": render_exitos,
    "faq": render_faq,
    "seccion_1": render_generic,
    "seccion_2": render_generic,
    "seccion_3": render_generic,
}


def mostrar_pie_de_pagina(cfg: FooterConfig | None = None) -> None:
    """Pinta el footer bajo las pestañas."""
    render_footer(cfg or FooterConfig())


def mostrar_paginas_en_pestanas() -> None:
    """Pinta cada vista dentro de su pestaña superior."""
    contenedores = render_tabs()
    for pagina in PAGINAS:
        with contenedores[pagina.id]:
            _RUTA_VISTAS[pagina.id]()
