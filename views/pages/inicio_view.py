"""
VISTA (MVC) — Página de inicio.
Presentación principal: cabecera con foto y CTA, puntos clave y reel en bucle.
"""
import base64
import mimetypes
import re
from pathlib import Path

import streamlit as st

from models.media_model import IMAGEN_VIDEO, VIDEO_PRINCIPAL
from models.perfil_model import PERFIL
from views.components.header_view import render_header
from views.utils_html import compactar_html

_CSS_PATH = Path(__file__).resolve().parents[1] / "styles" / "inicio.css"

_YT_PATRON = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|shorts/|embed/))([\w-]{11})"
)
_IG_PATRON = re.compile(r"instagram\.com/(?:reel|p|tv|reels)/([\w-]+)")
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


def _youtube_id(url: str) -> str | None:
    """Extrae el ID de un enlace de YouTube (watch, shorts, youtu.be)."""
    m = _YT_PATRON.search(url)
    return m.group(1) if m else None


def _instagram_id(url: str) -> str | None:
    """Extrae el ID de un enlace de Instagram (reel, post o IGTV)."""
    m = _IG_PATRON.search(url)
    return m.group(1) if m else None


def _fuente_video() -> tuple[str, str] | None:
    """Devuelve (src, tipo) donde tipo es youtube|instagram|directo."""
    fuente = VIDEO_PRINCIPAL.fuente
    if not fuente:
        return None
    if fuente.startswith(("http://", "https://")):
        yt_id = _youtube_id(fuente)
        if yt_id:
            src = (
                f"https://www.youtube-nocookie.com/embed/{yt_id}"
                f"?autoplay=1&mute=1&loop=1&playlist={yt_id}"
                f"&playsinline=1&rel=0"
            )
            return src, "youtube"
        ig_id = _instagram_id(fuente)
        if ig_id:
            return f"https://www.instagram.com/reel/{ig_id}/embed/caption/0", "instagram"
        return fuente, "directo"
    ruta = _ROOT / fuente
    if not ruta.exists():
        return None
    mime = mimetypes.guess_type(ruta.name)[0] or "video/mp4"
    b64 = base64.b64encode(ruta.read_bytes()).decode()
    return f"data:{mime};base64,{b64}", "directo"


def _imagen_data_uri() -> str | None:
    """Devuelve la imagen acompañante como data-URI, o None si no existe."""
    ruta = _ROOT / IMAGEN_VIDEO.ruta
    if not ruta.exists():
        return None
    mime = mimetypes.guess_type(ruta.name)[0] or "image/png"
    b64 = base64.b64encode(ruta.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def _render_video() -> None:
    fuente = _fuente_video()
    if not fuente:
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

    src, tipo = fuente
    if tipo == "youtube":
        reproductor = (
            f'<iframe class="inicio-reel__video" src="{src}" '
            'allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>'
        )
    elif tipo == "instagram":
        reproductor = (
            f'<iframe class="inicio-reel__video inicio-reel__video--ig" src="{src}" '
            'scrolling="no" allowfullscreen></iframe>'
        )
    else:
        reproductor = (
            f'<video class="inicio-reel__video" src="{src}" '
            "autoplay muted loop playsinline controls></video>"
        )

    img_uri = _imagen_data_uri()
    if img_uri:
        html = f"""
        <section class="inicio-duo">
            <div class="inicio-duo__item">{reproductor}</div>
            <div class="inicio-duo__item">
                <img class="inicio-duo__foto" src="{img_uri}" alt="{IMAGEN_VIDEO.alt}">
            </div>
        </section>
        """
    else:
        html = f"""
        <section class="inicio-video">
            <div class="inicio-reel">{reproductor}</div>
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
