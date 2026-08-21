"""
MODELO (MVC) — Datos del pie de página.
Solo contiene datos y configuración, sin lógica de presentación.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class FooterConfig:
    """Configuración inmutable del pie de página."""

    nombre_entidad: str = "Proyecto ABG · Luis"
    eslogan: str = "Seriedad. Temple. Compromiso profesional."
    anio: int = 2026
    version: str = "v1.0.0"

    enlaces: tuple = field(default_factory=lambda: (
        ("Aviso legal", "#"),
        ("Privacidad", "#"),
        ("Contacto", "#"),
    ))

    # Paleta corporativa: azul marino / gris profesional
    colores: dict = field(default_factory=lambda: {
        "fondo":        "#0A1628",  # azul marino profundo
        "fondo_alt":    "#0F1F38",  # azul marino medio
        "borde":        "#1E3A5F",  # línea divisoria azul acero
        "texto":        "#C9D4E4",  # gris azulado claro
        "texto_suave":  "#7E8CA3",  # gris pizarra
        "acento":       "#3B82C4",  # azul acero para hover/acento
    })

    def texto_derechos(self) -> str:
        return f"© {self.anio} {self.nombre_entidad} · Todos los derechos reservados"

    def linea_version(self) -> str:
        return f"{self.eslogan}  |  {self.version}"
