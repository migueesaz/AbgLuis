"""
MODELO (MVC) — Datos de la Biblioteca de Éxitos.
Registros de casos con resultado favorable.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Exito:
    titulo: str
    descripcion: str
    resultado: str
    anio: int


EXITOS: tuple[Exito, ...] = (
    Exito(
        titulo="Recuperación de cartera",
        descripcion="Recuperación integral de deuda impaga mediante acuerdo extrajudicial.",
        resultado="Resuelto a favor del cliente",
        anio=2025,
    ),
    Exito(
        titulo="Defensa laboral",
        descripcion="Reconocimiento de prestaciones y indemnización completa.",
        resultado="Sentencia favorable",
        anio=2025,
    ),
    Exito(
        titulo="Asesoría corporativa",
        descripcion="Constitución y blindaje societario de empresa comercial.",
        resultado="Contrato cerrado",
        anio=2026,
    ),
)
