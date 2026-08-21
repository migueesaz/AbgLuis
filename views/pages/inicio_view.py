"""
VISTA (MVC) — Página de inicio.
"""
import streamlit as st

from models.perfil_model import PERFIL
from views.components.header_view import render_header


def render_inicio() -> None:
    render_header(PERFIL)
    st.write("Contenido principal de la página…")
