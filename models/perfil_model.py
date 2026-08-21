"""
MODELO (MVC) — Datos del perfil profesional mostrado en la cabecera.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Perfil:
    nombre: str
    titulo: str
    foto_ruta: str  # relativa a la raíz del proyecto


PERFIL = Perfil(
    nombre="Luis Eduardo Sanchez Camargo",
    titulo="Especialista en Derecho Penal | Exfiscal del Ministerio Público",
    foto_ruta="assets/foto_perfil.jpg",
)
