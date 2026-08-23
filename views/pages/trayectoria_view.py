"""
VISTA (MVC) — Página "Trayectoria".
Presenta la trayectoria profesional en bloques con línea de tiempo.
Los datos provienen del modelo; actualmente son placeholders.
"""
from pathlib import Path

import streamlit as st

from models.exitos_model import EXITOS
from models.trayectoria_model import TRAYECTORIA, BloqueTrayectoria, EtapaTrayectoria
from views.utils_html import compactar_html

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "trayectoria.css"


def _etapa_html(etapa: EtapaTrayectoria) -> str:
    periodo = (
        f'<span class="tray-item__periodo">{etapa.periodo}</span>'
        if etapa.periodo
        else ""
    )
    detalle = f'<div class="tray-item__detalle">{etapa.detalle}</div>' if etapa.detalle else ""
    return f"""
    <div class="tray-item">
        <span class="tray-item__punto"></span>
        <div class="tray-item__cuerpo">
            {periodo}
            <div class="tray-item__titulo">{etapa.titulo}</div>
            {detalle}
        </div>
    </div>
    """


def _bloque_html(bloque: BloqueTrayectoria) -> str:
    etapas = "".join(_etapa_html(e) for e in bloque.etapas)
    return f"""
    <section class="tray-bloque">
        <h2 class="tray-bloque__titulo">{bloque.icono} {bloque.titulo}</h2>
        <div class="tray-timeline">{etapas}</div>
    </section>
    """


def render_trayectoria() -> None:
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

    st.title("🏛️ Trayectoria")
    st.caption("Recorrido profesional del abogado. Contenido en preparación.")

    for bloque in TRAYECTORIA:
        st.markdown(compactar_html(_bloque_html(bloque)), unsafe_allow_html=True)

    st.divider()
    st.subheader("Hitos destacados")
    cols = st.columns(2)
    for i, hito in enumerate(EXITOS):
        with cols[i % 2]:
            st.markdown(
                compactar_html(
                    f"""
                    <div class="exito-card">
                        <div class="exito-card__titulo">{hito.titulo}</div>
                        <div class="exito-card__pie">
                            <span class="exito-card__resultado">{hito.resultado}</span>
                            <span class="exito-card__anio">{hito.anio}</span>
                        </div>
                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )
