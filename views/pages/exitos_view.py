"""
VISTA (MVC) — Página "Biblioteca de Éxitos".
Renderiza los registros del modelo en tarjetas oscuras.
"""
from pathlib import Path

import streamlit as st

from models.exitos_model import EXITOS

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "exitos.css"


def _card_html(titulo: str, desc: str, resultado: str, anio: int) -> str:
    return f"""
    <div class="exito-card">
        <div class="exito-card__titulo">{titulo}</div>
        <div class="exito-card__desc">{desc}</div>
        <div class="exito-card__pie">
            <span class="exito-card__resultado">{resultado}</span>
            <span class="exito-card__anio">{anio}</span>
        </div>
    </div>
    """


def render_exitos() -> None:
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

    st.title("🏆 Biblioteca de Éxitos")
    st.caption("Casos resueltos con resultado favorable para nuestros clientes.")

    cols = st.columns(2)
    for i, exito in enumerate(EXITOS):
        with cols[i % 2]:
            st.markdown(
                _card_html(exito.titulo, exito.descripcion, exito.resultado, exito.anio),
                unsafe_allow_html=True,
            )
