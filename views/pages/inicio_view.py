"""
VISTA (MVC) — Página de inicio.
Presentación principal: cabecera con foto y CTA, puntos clave y reel en bucle.
"""
import base64
import mimetypes
from pathlib import Path

import streamlit as st

from models.media_model import VIDEO_PRINCIPAL
from models.perfil_model import PERFIL
from views.components.header_view import render_header
from views.utils_html import compactar_html

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "inicio.css"
_ROOT = Path(__file__).resolve().parents[2]

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


def _fuente_video() -> str | None:
    """Devuelve la fuente del video: URL directa, /static/ o data-URI."""
    fuente = VIDEO_PRINCIPAL.fuente
    if fuente.startswith(("http://", "https://")):
        return fuente
    ruta = _ROOT / fuente
    if not ruta.exists():
        return None
    if fuente.replace("\\", "/").startswith("static/"):
        from urllib.parse import quote
        return "/app/" + quote(fuente.replace("\\", "/"))
    mime = mimetypes.guess_type(ruta.name)[0] or "video/mp4"
    b64 = base64.b64encode(ruta.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def _poster_video() -> str:
    """Imagen de previsualización del video (data-URI de la foto de perfil)."""
    ruta = _ROOT / PERFIL.foto_ruta
    if not ruta.exists():
        return ""
    mime = mimetypes.guess_type(ruta.name)[0] or "image/jpeg"
    b64 = base64.b64encode(ruta.read_bytes()).decode()
    return f' poster="data:{mime};base64,{b64}"'


def _render_video() -> None:
    src = _fuente_video()
    if not src:
        st.markdown(
            compactar_html(
                f"""
                <section class="inicio-video">
                    <div class="inicio-video__marco">
                        <span class="inicio-video__play"></span>
                        <p class="inicio-video__texto">Video de presentación — próximamente</p>
                    </div>
                </section>
                """
            ),
            unsafe_allow_html=True,
        )
        return

    st.subheader(f"🎬 {VIDEO_PRINCIPAL.titulo}")
    if VIDEO_PRINCIPAL.descripcion:
        st.caption(VIDEO_PRINCIPAL.descripcion)
    html = f"""
    <section class="inicio-video">
        <div class="inicio-reel">
            <video class="inicio-reel__video" src="{src}"{_poster_video()} autoplay muted loop playsinline controls preload="metadata"></video>
        </div>
    </section>
    """
    st.markdown(compactar_html(html), unsafe_allow_html=True)


def render_inicio() -> None:
    st.markdown(f"<style>{_CSS_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    render_header(PERFIL)

    puntos = "".join(_punto_html(i, t, d) for i, t, d in _PUNTOS_CLAVE)
    st.markdown(compactar_html(f'<section class="inicio-puntos">{puntos}</section>'), unsafe_allow_html=True)

    st.divider()
    _render_video()
