"""
main.py — Punto de arranque de Caine.

Esta es una versión mínima ("Hola, soy Caine") para comprobar que tu entorno
funciona. Todavía NO usa un modelo de IA; es solo el esqueleto sobre el que
construirás. Ejecuta:  python src/caine/main.py
"""


def saludar() -> str:
    """Devuelve el saludo de Caine. Tu primera función."""
    return "🎪 Hola, soy Caine. Algún día crearé mundos enteros... dame tiempo."


def main() -> None:
    print(saludar())
    print("Entorno listo. Empieza a construir desde aquí.")


if __name__ == "__main__":
    main()
