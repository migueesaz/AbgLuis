"""
VISTA (MVC) — Utilidades para renderizar HTML en Streamlit.

Streamlit interpreta líneas con sangría de 4+ espacios después de una
línea en blanco como bloques de código de Markdown y muestra el HTML
como texto. Esta utilidad elimina sangrías y líneas vacías.
"""
import re


def compactar_html(html: str) -> str:
    """Quita sangrías y líneas vacías para evitar bloques de código Markdown."""
    return "\n".join(
        linea.strip()
        for linea in re.split(r"\r?\n", html)
        if linea.strip()
    )
