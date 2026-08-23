"""
Punto de entrada de la aplicación (Streamlit).
Estructura MVC:  models/ · views/ · controllers/

Navegación por pestañas superiores (st.tabs) — sin st.navigation.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st

from controllers.main_controller import mostrar_paginas_en_pestanas, mostrar_pie_de_pagina
from views.components.header_view import render_marca

st.set_page_config(
    page_title="LEX · Luis Eduardo Sanchez Camargo",
    page_icon="⚖️",
    layout="wide",
)

# --- Branding global LEX (por encima de redes y navegación) ---
render_marca()

# --- Páginas en pestañas superiores (MVC) ---
mostrar_paginas_en_pestanas()

# --- Pie de página común ---
mostrar_pie_de_pagina()
