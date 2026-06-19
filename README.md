# 🌌 TheCosmos

> Un agente generativo con personalidad, memoria y la capacidad de crear y dar
> vida a su propio mundo virtual. La inteligencia que habita y dirige
> *TheCosmos* se llama **Caine**.

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Licencia](https://img.shields.io/badge/licencia-MIT-green)

---

## ✨ Sobre el proyecto

**TheCosmos** es un proyecto personal —con la vista puesta en convertirse en mi
Trabajo de Fin de Grado— que explora una pregunta: *¿hasta dónde puede una IA
generativa crear, poblar y dirigir un mundo virtual de forma autónoma?*

El sistema combina un **modelo de lenguaje** (el "cerebro"), un **agente** con
memoria y capacidad de decisión, y un **motor de videojuego** donde Caine
materializa objetos, personajes y escenarios en respuesta a lo que ocurre.

### ¿Qué es y qué no es?

Por honestidad con el alcance: TheCosmos **no** busca crear una IA consciente
(eso sería una AGI, hoy inexistente). Es una **simulación convincente**: un
agente que genera ideas, conversa con personalidad, recuerda y actúa sobre un
mundo. El objetivo es la ilusión creíble, no la consciencia.

---

## 🧩 Arquitectura

```
   ┌─────────────────────────┐         JSON          ┌──────────────────────┐
   │        IA (Python)      │  <----------------->  │   Juego (Unity/C#)   │
   │                         │                       │                      │
   │  LLM  →  Agente         │   "crea un globo"     │  Mundo 3D, físicas,  │
   │          ↕              │   "ha pasado X"       │  personajes, objetos │
   │        Memoria          │                       │                      │
   └─────────────────────────┘                       └──────────────────────┘
            (Caine)
```

El "cerebro" (Caine) y el "mundo" son dos programas separados que se comunican
por mensajes JSON. Así pueden desarrollarse de forma independiente.

---

## 📁 Estructura del repositorio

```
TheCosmos/
├── ia/            # El cerebro. Todo en Python (LLM, agente, memoria).
├── juego/         # El mundo. Unity + C# (fase posterior).
├── compartido/    # El "contrato" de mensajes entre la IA y el juego.
└── docs/          # Roadmap, arquitectura, diario de progreso.
```

---

## 🛠️ Tecnologías

**En uso:**
- Python — cerebro de la IA

**Previstas:**
- Modelos de lenguaje vía API (Claude / OpenAI) y modelos locales (Ollama)
- Framework de agentes (LangGraph / CrewAI)
- Base de datos vectorial (ChromaDB) para la memoria
- Unity + C# para el mundo virtual

---

## 🗺️ Roadmap

- [x] **Fase 0** — Estructura del repositorio y entorno de trabajo
- [ ] **Fase 1** — Fundamentos de Python ⬅️ *en curso*
- [ ] **Fase 2** — Caine conversacional (LLM + personalidad)
- [ ] **Fase 3** — Memoria y agencia (recordar y decidir)
- [ ] **Fase 4** — El mundo en Unity
- [ ] **Fase 5** — Integración IA ⇄ juego

---

## 🚀 Puesta en marcha

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/TheCosmos.git
cd TheCosmos/ia

# Crear y activar el entorno virtual
python -m venv .venv
# Windows:   .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Probar que arranca
python src/caine/main.py
```

---

## 📓 Diario de progreso

Llevo un registro del avance día a día en [`docs/diario.md`](docs/diario.md).

---

## 👤 Autor

**Alejandro de la Peña**
Universidad Europea del Atlántico
📧 alejandrodelapena@alumnos.uneatlantico.es
🔗 LinkedIn — *próximamente*

---

## 📄 Licencia

Distribuido bajo licencia MIT. Consulta el archivo [`LICENSE`](LICENSE) para más
información.
