"""
VISTA (MVC) — Cabecera principal con fotografía, nombre y título.
Si no existe la foto, muestra un avatar con las iniciales.
"""
import base64
import mimetypes
from pathlib import Path

import streamlit as st

from models.perfil_model import Perfil, enlace_whatsapp

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

    descripcion_html = ""
    if perfil.descripcion:
        descripcion_html = f'<p class="hero-header__descripcion">{perfil.descripcion}</p>'

    cta_html = ""
    if perfil.whatsapp_numero:
        cta_html = f"""
        <div class="hero-header__cta">
            <a class="btn-whatsapp" href="{enlace_whatsapp()}" target="_blank" rel="noopener">
                <svg class="btn-whatsapp__icono" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9.4 3 4 8.3 4 14.9c0 2.6.8 5 2.3 7L4.6 28l6.3-1.6c1.9 1 4 1.6 6.2 1.6h.1c6.6 0 12-5.3 12-11.9C29.2 8.3 22.6 3 16 3zm7 16.9c-.3.8-1.7 1.6-2.4 1.7-.6.1-1.4.1-2.3-.1-.5-.2-1.2-.4-2-.8-3.6-1.6-5.9-5.2-6.1-5.4-.2-.2-1.4-1.9-1.4-3.6 0-1.7.9-2.6 1.2-2.9.3-.3.7-.4 1-.4h.7c.2 0 .5-.1.8.6.3.8 1.1 2.6 1.2 2.8.1.2.2.4 0 .7-.1.3-.2.4-.4.7l-.6.7c-.2.2-.4.4-.2.8.2.4 1 1.7 2.2 2.7 1.5 1.4 2.8 1.8 3.2 2 .4.2.6.2.9-.1.2-.3 1-1.2 1.3-1.6.3-.4.6-.3.9-.2.3.1 2.1 1 2.5 1.2.4.2.6.3.7.4.1.3.1.9-.2 1.8z"/></svg>
                Contactar por WhatsApp
            </a>
            <span class="hero-header__nota">Atención rápida y confidencial</span>
        </div>
        """

    return f"""
    <header class="hero-header">
        {foto_html}
        <div class="hero-header__contenido">
            <h1 class="hero-header__nombre">{perfil.nombre}</h1>
            <p class="hero-header__titulo">{titulo}</p>
            {descripcion_html}
            {cta_html}
        </div>
    </header>
    """


def render_header(perfil: Perfil) -> None:
    """Pinta la cabecera principal del inicio."""
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    st.markdown(_build_html(perfil), unsafe_allow_html=True)
