"""
VISTA (MVC) — Pestañas superiores para las páginas.
Crea una pestaña por cada página registrada en el modelo.
"""
import streamlit as st

from models.navegacion_model import PaginaConfig, PAGINAS


def render_tabs() -> dict[str, object]:
    """Devuelve {id_de_pagina: contenedor_de_pestaña}.

    Si la página no tiene título, la pestaña muestra solo el ícono.
    """
    etiquetas = [f"{p.icono} {p.titulo}".strip() for p in PAGINAS]
    pestanas = st.tabs(etiquetas)
    return {p.id: cont for p, cont in zip(PAGINAS, pestanas)}
