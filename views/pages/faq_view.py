"""
VISTA (MVC) — Página "Preguntas Frecuentes".
Renderiza las preguntas del modelo en expandidores oscuros.
"""
from pathlib import Path

import streamlit as st

from models.faq_model import PREGUNTAS_FRECUENTES

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "faq.css"


def render_faq() -> None:
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

    st.title("❓ Preguntas Frecuentes")
    st.caption("Respuestas rápidas a las dudas más comunes de nuestros clientes.")

    for item in PREGUNTAS_FRECUENTES:
        with st.expander(item.pregunta):
            st.write(item.respuesta)
