"""
VISTA (MVC) — Página de inicio.
Presentación principal: cabecera con foto y CTA, más franja de puntos clave.
"""
from pathlib import Path

import streamlit as st

from models.perfil_model import PERFIL
from views.components.header_view import render_header
from views.utils_html import compactar_html

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "inicio.css"

_PUNTOS_CLAVE = (
    ("🎯", "Defensa penal estratégica", "Diseño de la estrategia según cada caso."),
    ("🏛️", "Experiencia desde el Estado", "Trayectoria como fiscal del Ministerio Público."),
    ("🤝", "Acompañamiento cercano", "Comunicación clara en cada etapa del proceso."),
)


def _punto_html(icono: str, titulo: str, texto: str) -> str:
    return f"""
    <div class="inicio-punto">
        <span class="inicio-punto__icono">{icono}</span>
        <div>
            <div class="inicio-punto__titulo">{titulo}</div>
            <div class="inicio-punto__texto">{texto}</div>
        </div>
    </div>
    """


def render_inicio() -> None:
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    render_header(PERFIL)

    puntos = "".join(_punto_html(i, t, d) for i, t, d in _PUNTOS_CLAVE)
    st.markdown(compactar_html(f'<section class="inicio-puntos">{puntos}</section>'), unsafe_allow_html=True)
