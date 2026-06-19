"""
Prueba básica ("smoke test"): comprueba que el código mínimo funciona.
Ejecuta desde la carpeta ia/ con:  pytest
"""
from src.caine.main import saludar


def test_caine_saluda():
    resultado = saludar()
    assert "Caine" in resultado
