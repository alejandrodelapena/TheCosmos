# Arquitectura (visión general)

```
   ┌─────────────────────────┐         JSON          ┌──────────────────────┐
   │        IA (Python)      │  <----------------->  │   Juego (Unity/C#)   │
   │                         │                       │                      │
   │  LLM  →  Agente         │   "crea un globo"     │  Mundo 3D, físicas,  │
   │          ↕              │   "ha pasado X"       │  personajes, objetos │
   │        Memoria          │                       │                      │
   └─────────────────────────┘                       └──────────────────────┘
```

- **LLM**: genera ideas, diálogo y personalidad.
- **Agente**: decide qué hacer y traduce decisiones en eventos para el juego.
- **Memoria**: recuerda lo hablado y lo ocurrido.
- **Juego**: ejecuta lo que el agente pide y devuelve lo que ocurre.

Mantén estas piezas desacopladas: podrás mejorar una sin romper las demás.
