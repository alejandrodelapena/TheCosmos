# IA — El cerebro de Caine

Todo el código de inteligencia artificial vive aquí. Está en **Python**.

## Estructura

```
ia/
├── src/caine/
│   ├── main.py        # Punto de entrada: arranca a Caine.
│   ├── llm/           # Hablar con el modelo de lenguaje (API o local).
│   ├── agente/        # Lógica de decisiones y uso de herramientas.
│   └── memoria/       # Recordar conversaciones y hechos.
├── tests/             # Pruebas automáticas.
├── notebooks/         # Experimentos sueltos en Jupyter.
├── requirements.txt   # Librerías que necesita el proyecto.
└── .env.example       # Plantilla de variables (copia a .env y rellena).
```

## Puesta en marcha (primera vez)

```bash
# 1. Crear un entorno virtual aislado
python -m venv .venv

# 2. Activarlo
#    Windows:   .venv\Scripts\activate
#    Mac/Linux: source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Copiar la plantilla de secretos y rellenar tu clave de API
#    Windows:   copy .env.example .env
#    Mac/Linux: cp .env.example .env

# 5. Probar que arranca
python src/caine/main.py
```

## Regla de oro

El archivo `.env` (con tus claves) **nunca** se sube a GitHub. Ya está
protegido en el `.gitignore`.
