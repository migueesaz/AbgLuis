"""
VISTA (MVC) — Pestañas superiores para las páginas.
Crea una pestaña por cada página registrada en el modelo y, a la derecha,
los botones de redes sociales.
"""
from pathlib import Path

import streamlit as st

from models.navegacion_model import PaginaConfig, PAGINAS
from models.redes_model import REDES_SOCIALES
from views.utils_html import compactar_html

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "redes.css"

_ICONOS = {
    "Instagram": (
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<rect x="2.5" y="2.5" width="19" height="19" rx="5.5" fill="none" '
        'stroke="currentColor" stroke-width="2"/>'
        '<circle cx="12" cy="12" r="4.5" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<circle cx="17.3" cy="6.7" r="1.3" fill="currentColor"/></svg>'
    ),
    "TikTok": (
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" '
        'd="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 '
        "1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 "
        "2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 "
        "1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 "
        '1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>'
    ),
}


def _botones_redes_html() -> str:
    enlaces = "".join(
        f'<a class="btn-red" href="{red.url}" target="_blank" rel="noopener" '
        f'aria-label="{red.nombre}" title="{red.nombre}">{_ICONOS.get(red.nombre, "")}</a>'
        for red in REDES_SOCIALES
    )
    return f'<nav class="barra-redes">{enlaces}</nav>'


def render_tabs() -> dict[str, object]:
    """Devuelve {id_de_pagina: contenedor_de_pestaña}.

    Si la página no tiene título, la pestaña muestra solo el ícono.
    Los botones de redes se alinean a la derecha de la barra.
    """
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

    col_pestanas, col_redes = st.columns([10, 1], vertical_alignment="top")
    with col_redes:
        st.markdown(compactar_html(_botones_redes_html()), unsafe_allow_html=True)
    with col_pestanas:
        etiquetas = [f"{p.icono} {p.titulo}".strip() for p in PAGINAS]
        pestanas = st.tabs(etiquetas)

    return {p.id: cont for p, cont in zip(PAGINAS, pestanas)}
