"""
VISTA (MVC) — Cabecera principal con fotografía, nombre y título.
Si no existe la foto, muestra un avatar con las iniciales.
"""
import base64
import mimetypes
from pathlib import Path

import streamlit as st

from models.perfil_model import Perfil

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "header.css"
_ROOT = Path(__file__).resolve().parents[2]


def _foto_data_uri(perfil: Perfil) -> str | None:
    ruta = _ROOT / perfil.foto_ruta
    if not ruta.exists():
        return None
    mime = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"
    b64 = base64.b64encode(ruta.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def _iniciales(nombre: str) -> str:
    palabras = nombre.split()
    primera = palabras[0][0]
    apellido = palabras[2][0] if len(palabras) >= 3 else palabras[-1][0]
    return (primera + apellido).upper()


def _build_html(perfil: Perfil) -> str:
    data_uri = _foto_data_uri(perfil)
    if data_uri:
        foto_html = f'<img class="hero-header__foto" src="{data_uri}" alt="Fotografía de {perfil.nombre}">'
    else:
        foto_html = f'<div class="hero-header__avatar">{_iniciales(perfil.nombre)}</div>'

    titulo = perfil.titulo.replace("|", '<span class="sep">|</span>')
    return f"""
    <header class="hero-header">
        {foto_html}
        <div>
            <h1 class="hero-header__nombre">{perfil.nombre}</h1>
            <p class="hero-header__titulo">{titulo}</p>
        </div>
    </header>
    """


def render_header(perfil: Perfil) -> None:
    """Pinta la cabecera principal del inicio."""
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    st.markdown(_build_html(perfil), unsafe_allow_html=True)
