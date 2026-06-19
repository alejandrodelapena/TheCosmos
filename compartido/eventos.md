# Contrato de eventos: IA ⇄ Juego

La IA y el juego son dos programas separados que se hablan con mensajes JSON.
Definir aquí ese "idioma común" desde el principio te ahorrará muchos líos.

## Ejemplo: la IA pide al juego que aparezca un objeto

```json
{
  "tipo": "crear_objeto",
  "objeto": "globo",
  "posicion": { "x": 0, "y": 1, "z": 3 },
  "color": "rojo"
}
```

## Ejemplo: el juego informa a la IA de algo que ha pasado

```json
{
  "tipo": "jugador_dice",
  "texto": "Caine, hazme una montaña rusa"
}
```

Empieza con 3-4 tipos de evento sencillos y ve ampliando. La clave es que
ambos lados (Python y C#) entiendan exactamente la misma estructura.
