"""
VISTA (MVC) — Renderizado del pie de página.
Convierte los datos del modelo en HTML/CSS. Sin lógica de negocio.
"""
from pathlib import Path

import streamlit as st

from models.footer_model import FooterConfig

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "footer.css"


def _build_html(cfg: FooterConfig) -> str:
    enlaces = "".join(
        f'<a href="{url}">{texto}</a>' for texto, url in cfg.enlaces
    )
    return f"""
    <div class="app-footer">
        <div class="app-footer__grid">
            <div>
                <div class="app-footer__brand">{cfg.nombre_entidad}</div>
                <div class="app-footer__tagline">{cfg.eslogan}</div>
            </div>
            <nav class="app-footer__links">{enlaces}</nav>
        </div>
        <div class="app-footer__bottom">
            <span>{cfg.texto_derechos()}</span>
            <span class="app-footer__version">{cfg.version}</span>
        </div>
    </div>
    """


def render_footer(cfg: FooterConfig | None = None) -> None:
    """Pinta el pie de página al final de la página."""
    cfg = cfg or FooterConfig()
    css = _CSS_PATH.read_text(encoding="utf-8")

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.markdown(_build_html(cfg), unsafe_allow_html=True)
