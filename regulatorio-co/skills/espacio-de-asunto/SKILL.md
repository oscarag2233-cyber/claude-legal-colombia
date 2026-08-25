---
name: espacio-de-asunto
description: >
  Crea, cambia, lista y cierra espacios de asunto para Regulatorio y Vigilancia Normativa, cuando se quiere que
  el contexto y las salidas queden aislados por caso o por cliente. Actívela cuando el
  usuario hable de trabajar «por casos», «por expedientes» o «por cliente», o cuando
  pida separar lo que hoy está mezclado.
---

# Espacio de asunto — Regulatorio y Vigilancia Normativa

## Para qué

Por defecto, este plugin trabaja **a nivel de práctica**: un solo perfil, un solo
contexto, todas las salidas juntas. Eso le sirve a la mayoría de usuarios in-house.

Quien lleva casos de varios clientes necesita lo contrario: que el contexto de un caso
no se filtre a otro, que las salidas queden en la carpeta del caso, y que el conflicto
de interés no se vuelva un accidente de archivo.

## Estructura

```
~/.claude/plugins/config/claude-legal-colombia/regulatorio-co/
  CLAUDE.md                    # perfil de práctica (aplica a todos los asuntos)
  bitacora-verificacion.md
  asuntos/
    <slug-del-asunto>/
      asunto.md                # partes, radicado, contexto y anulaciones locales
      terminos.md              # términos vivos de este asunto
      salidas/                 # lo que produzcan las skills
```

## Comandos

| Uso | Qué hace |
|---|---|
| `/regulatorio-co:espacio-de-asunto habilitar` | Enciende la maquinaria de asuntos y lo registra en el perfil |
| `/regulatorio-co:espacio-de-asunto crear <slug>` | Crea el asunto y hace la entrevista corta de contexto |
| `/regulatorio-co:espacio-de-asunto cambiar <slug>` | Fija el asunto activo |
| `/regulatorio-co:espacio-de-asunto listar` | Lista los asuntos con su estado y su próximo término |
| `/regulatorio-co:espacio-de-asunto cerrar <slug>` | Cierra el asunto y deja la nota de cierre |
| `/regulatorio-co:espacio-de-asunto practica` | Vuelve a trabajar a nivel de práctica |

## Entrevista corta al crear un asunto

1. ¿Cómo se llama el asunto y quién es el cliente?
2. ¿Cuáles son las partes? *(Anotarlas todas: es lo que después permite detectar
   conflicto de interés.)*
3. ¿Hay radicado, número de proceso o expediente administrativo?
4. ¿Ante qué autoridad o foro?
5. ¿Hay algún término corriendo hoy? *(Si lo hay, se registra de una vez en
   `terminos.md` con su norma.)*
6. ¿Hay algo del perfil de práctica que en este asunto sea distinto?

## Reglas duras

- **No se leen archivos de otro asunto** salvo que `Contexto entre asuntos` esté en
  `on` en el perfil. Por defecto está en `off`.
- **Detección de conflicto.** Al crear un asunto, cotejar las partes contra los asuntos
  existentes. Si una parte del nuevo asunto figura como contraparte en otro, **detenerse
  y avisar**: «[Nombre] figura como contraparte en el asunto [X]. Esto puede ser un
  conflicto de interés (Ley 1123 de 2007, art. 34 lit. b y c). Revíselo antes de que yo
  siga trabajando en este asunto.» No continuar sin confirmación expresa.
- **Las salidas van a la carpeta del asunto**, no al directorio del plugin.
- **Al cerrar**, dejar nota de cierre: qué se hizo, qué quedó pendiente, qué términos
  siguen vivos y qué marcas `[verificar]` quedaron sin resolver.

## Si los asuntos están deshabilitados

Cuando una skill pregunte por el asunto activo y la maquinaria esté apagada, no
preguntar nada: trabajar a nivel de práctica en silencio. El usuario in-house nunca
debería ver esta capa.
