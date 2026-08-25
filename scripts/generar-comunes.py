#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el andamiaje común de todos los plugins de claude-legal-colombia.

Emite, para cada plugin del registro:
  <slug>/.claude-plugin/plugin.json
  <slug>/.mcp.json
  <slug>/hooks/hooks.json
  <slug>/.gitignore
  <slug>/CLAUDE.md          (plantilla de perfil de práctica)
  <slug>/README.md
  <slug>/skills/entrevista-inicial/SKILL.md
  <slug>/skills/personalizar/SKILL.md
  <slug>/skills/verificar-citas/SKILL.md
  <slug>/skills/espacio-de-asunto/SKILL.md

Y en la raíz: .claude-plugin/marketplace.json

Las skills propias de cada plugin se escriben a mano y NO se tocan aquí.

Uso:  python3 scripts/generar-comunes.py
"""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

import registro as R           # noqa: E402
import _bloques as B           # noqa: E402

VERSION = "1.0.0"


def esc(t, slug):
    return (t.replace("{CFG}", B.CFG)
             .replace("{SLUG}", slug)
             .replace("{MARCA}", B.MARCA))


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    if not contenido.endswith("\n"):
        contenido += "\n"
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)


def json_escribir(ruta, obj):
    escribir(ruta, json.dumps(obj, ensure_ascii=False, indent=2))


# --------------------------------------------------------------------------
# marketplace.json
# --------------------------------------------------------------------------
def gen_marketplace():
    entradas = []
    for p in R.PLUGINS:
        entradas.append({
            "name": p["slug"],
            "displayName": p["display"],
            "source": "./" + p["slug"],
            "description": p["desc"],
            "author": dict(R.MARKETPLACE["author"]),
        })
    entradas.sort(key=lambda e: e["name"].lower())
    obj = {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": R.MARKETPLACE["name"],
        "description": R.MARKETPLACE["description"],
        "owner": R.MARKETPLACE["owner"],
        "plugins": entradas,
    }
    json_escribir(os.path.join(RAIZ, ".claude-plugin", "marketplace.json"), obj)


# --------------------------------------------------------------------------
# CLAUDE.md — plantilla de perfil de práctica
# --------------------------------------------------------------------------
def bloque_normas(p):
    filas = "\n".join("| %s | %s |" % (n, d) for n, d in p["normas"])
    return ("## Marco normativo de referencia\n\n"
            "*Punto de partida, no lista cerrada. Toda norma se verifica vigente antes de\n"
            "aplicarla: derogatorias, inexequibilidades, exequibilidades condicionadas y\n"
            "decretos reglamentarios posteriores cambian el resultado. Ver\n"
            "`referencias/jerarquia-normativa.md`.*\n\n"
            "| Norma | Qué gobierna |\n|---|---|\n" + filas + "\n\n"
            "**Estado de verificación de esta tabla:** `[PENDIENTE — registrar fecha de la última\n"
            "revisión de vigencia y quién la hizo]`\n")


def bloque_autoridades(p):
    items = "\n".join("- " + a for a in p["autoridades"])
    return ("## Autoridades y foros habituales\n\n" + items +
            "\n\n**Ciudades y circuitos donde actuamos:** [PENDIENTE]\n")


def bloque_integraciones(p):
    filas = "\n".join("| %s | [PENDIENTE ✓/✗] | %s |" % (n, f) for n, f in p["integraciones"])
    return ("## Integraciones disponibles\n\n"
            "| Integración | Estado | Qué hacemos si no está |\n|---|---|---|\n" + filas +
            "\n\n*Revisar de nuevo: `/%s:entrevista-inicial --revisar-integraciones`*\n" % p["slug"])


def bloque_criterios(p):
    if p.get("criterios"):
        return "## Criterios de la casa\n\n" + p["criterios"]
    secciones = "\n\n".join(
        "#### %s\n**Posición:** [PENDIENTE]\n**Alternativa aceptable:** [PENDIENTE]\n**Nunca:** [PENDIENTE]" % d
        for d in p.get("decisiones", []))
    return ("## Criterios de la casa\n\n"
            "*Cada criterio tiene tres niveles. Si una casilla dice `[PENDIENTE]`, la skill\n"
            "correspondiente pregunta antes de calificar; no asume.*\n\n"
            "### Decisiones que este plugin necesita resueltas\n\n" + secciones +
            "\n\n#### Lo único innegociable\n[PENDIENTE — la posición que se revisa de primera en todo asunto de esta área]\n")


def bloque_escalamiento(p):
    return ("## Escalamiento\n\n"
            "| Quién puede decidir | Sin escalar | Escala a | Por qué medio |\n|---|---|---|---|\n"
            "| [Dependiente / estudiante] | [PENDIENTE] | [Abogado] | [PENDIENTE] |\n"
            "| [Abogado] | [PENDIENTE] | [Socio / Director jurídico] | [PENDIENTE] |\n"
            "| [Socio / Director jurídico] | [PENDIENTE] | [Cliente / Junta] | [PENDIENTE] |\n\n"
            "**Umbrales en dinero o en SMLMV:** [PENDIENTE]\n\n"
            "**Escalamientos automáticos, sin importar la cuantía:**\n"
            "- Cualquier asunto con término que venza en menos de 5 días hábiles\n"
            "- Cualquier posición de la lista «Nunca» de los criterios de la casa\n"
            "- Cualquier asunto con exposición penal o disciplinaria\n"
            "- [PENDIENTE — añadir los propios]\n")


def bloque_estilo(p):
    return ("## Estilo de la casa\n\n"
            "**Tratamiento en escritos:** [PENDIENTE]\n\n"
            "**Extensión típica de un concepto:** [PENDIENTE]\n\n"
            "**Dónde queda el producto de trabajo:** [PENDIENTE]\n\n"
            "**A dónde van las alertas de términos:** [PENDIENTE]\n")


def gen_claude_md(p):
    slug = p["slug"]
    partes = [
        esc(B.CABECERA_CONFIG, slug),
        "",
        "# Perfil de práctica — %s" % p["display"],
        "",
        "*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta\n"
        "entonces es una plantilla. Si ve valores `[PENDIENTE]`, corra\n"
        "`/%s:entrevista-inicial`.*" % slug,
        "",
        "*Una vez diligenciado: edítelo directamente. Todas las skills de este plugin lo leen\n"
        "antes de hacer nada. Corrija algo aquí y queda corregido en todas partes.*",
        "",
        "**Ámbito:** " + p["ambito"],
        "",
        "---",
        "",
        "## Quiénes somos\n\n"
        "*(Nombre, tipo de organización, sector y tamaño vienen de `perfil-organizacion.md` —\n"
        "editar allá para cambiarlo en todos los plugins. Lo de aquí es propio de esta área.)*\n\n"
        "**Equipo de esta área:** [PENDIENTE]\n\n"
        "**Volumen típico:** [PENDIENTE — cuántos asuntos por mes]\n\n"
        "**Lo que más duele hoy:** [PENDIENTE — en palabras del equipo]\n\n"
        "**Entorno de práctica:** [PENDIENTE — Firma/litigante | In-house | Ambos]",
        "",
        "---",
        "",
        "## Quién usa esto\n\n"
        "**Rol:** [PENDIENTE — Abogado con tarjeta profesional | Estudiante o dependiente judicial | Personal no jurídico con acceso a abogado | Personal no jurídico sin acceso a abogado]\n\n"
        "**Abogado responsable:** [PENDIENTE — nombre y T.P.]\n\n"
        "**Tarjeta profesional vigente:** [PENDIENTE ✓/✗]",
        "",
        "---",
        "",
        bloque_integraciones(p),
        "---",
        "",
        bloque_normas(p),
        "---",
        "",
        bloque_autoridades(p),
        "---",
        "",
        bloque_criterios(p),
        "---",
        "",
        bloque_escalamiento(p),
        "---",
        "",
        bloque_estilo(p),
        "---",
        "",
        esc(B.SALIDAS, slug),
        "",
        "---",
        "",
        esc(B.POSTURA, slug),
        "",
        "---",
        "",
        esc(B.GUARDARRAILES, slug),
        "",
        "---",
        "",
        esc(B.ANDAMIAJE, slug),
        "",
        "---",
        "",
        esc(B.CIERRE_COMUN, slug),
        "",
        "---",
        "",
        p.get("preferencias", "").strip(),
    ]
    return "\n".join(x for x in partes if x is not None)


# --------------------------------------------------------------------------
# README del plugin
# --------------------------------------------------------------------------
def gen_readme(p):
    slug = p["slug"]
    comunes = [
        ("entrevista-inicial", "Entrevista de arranque. Levanta el perfil de práctica, los criterios de la casa y el estado de las integraciones. **Córrala primero.**"),
        ("personalizar", "Ajusta el perfil sin repetir la entrevista completa: cambiar una posición, un umbral, un destinatario."),
        ("verificar-citas", "Compuerta de verificación: toma una pieza y revisa cada norma, sentencia y término citado contra fuente oficial, dejando marcado lo que no se pudo confirmar."),
        ("espacio-de-asunto", "Crea, cambia y cierra espacios de asunto cuando se quiere aislar contexto y salidas por caso."),
    ]
    filas_p = "\n".join("| `/%s:%s` | %s |" % (slug, s, d) for s, d in p["propias"])
    filas_c = "\n".join("| `/%s:%s` | %s |" % (slug, s, d) for s, d in comunes)
    agentes = ""
    if p.get("agentes"):
        fa = "\n".join("| `%s` | %s |" % (a, d) for a, d in p["agentes"])
        agentes = ("\n## Agentes\n\n| Agente | Qué hace |\n|---|---|\n" + fa +
                   "\n\nLos agentes corren en la periodicidad que se configure y escriben en el\n"
                   "destino definido en el perfil de práctica. No radican, no firman y no deciden.\n")
    normas = "\n".join("- **%s** — %s" % (n, d) for n, d in p["normas"][:8])
    nohace = p.get("no_hace") or [
        "Emitir asesoría jurídica. Todo lo que produce es borrador para revisión de abogado",
        "Radicar, firmar, notificar o comunicarse con autoridades o contrapartes por su cuenta",
        "Afirmar que una cita está verificada cuando no la recuperó de fuente oficial",
        "Decidir por usted una calificación jurídica discutible: la marca y la escala",
    ]
    return "\n".join([
        "# %s" % p["display"],
        "",
        p["desc"],
        "",
        "> **Todo lo que produce este plugin es un borrador sujeto a revisión profesional.**",
        "> No es concepto jurídico ni asesoría, y no reemplaza a un abogado titulado e inscrito.",
        "> Ver [AVISO-LEGAL.md](../AVISO-LEGAL.md).",
        "",
        "**Ámbito:** " + p["ambito"],
        "",
        "## Instalación",
        "",
        "```bash",
        "/plugin marketplace add oscarag2233-cyber/claude-legal-colombia",
        "/plugin install %s@claude-legal-colombia" % slug,
        "```",
        "",
        "Luego, sin excepción:",
        "",
        "```bash",
        "/%s:entrevista-inicial" % slug,
        "```",
        "",
        "Sin la entrevista, las skills se detienen: prefieren no responder a responder genérico.",
        "",
        "## Skills",
        "",
        "### Propias del área",
        "",
        "| Skill | Qué hace |",
        "|---|---|",
        filas_p,
        "",
        "### Comunes a todos los plugins",
        "",
        "| Skill | Qué hace |",
        "|---|---|",
        filas_c,
        agentes,
        "## Marco normativo que aplica",
        "",
        normas,
        "",
        "La tabla completa, con su estado de verificación, está en el `CLAUDE.md` del plugin.",
        "",
        "## Lo que este plugin NO hace",
        "",
        "\n".join("- " + x for x in nohace),
        "",
        "## Configuración",
        "",
        "La configuración del usuario vive en",
        "`~/.claude/plugins/config/claude-legal-colombia/%s/CLAUDE.md`," % slug,
        "fuera del control de versiones. El `CLAUDE.md` de este directorio es la **plantilla**",
        "que la entrevista inicial copia allá.",
        "",
        "El perfil de la organización, compartido por todos los plugins, vive en",
        "`~/.claude/plugins/config/claude-legal-colombia/perfil-organizacion.md`.",
    ])


# --------------------------------------------------------------------------
# Skills comunes
# --------------------------------------------------------------------------
def skill_entrevista(p):
    slug = p["slug"]
    decisiones = p.get("decisiones") or []
    bloque_dec = "\n".join("- %s" % d for d in decisiones) or "- [las posiciones de la sección `## Criterios de la casa` de la plantilla]"
    integ = "\n".join("- %s" % n for n, _ in p["integraciones"])
    return esc("""---
name: entrevista-inicial
description: >
  Entrevista de arranque del plugin {DISPLAY}. Levanta el perfil de la organización, el
  perfil de práctica del área, los criterios de la casa, el escalamiento y el estado de
  las integraciones, y los escribe en la configuración del usuario. Es la única skill
  que corre sin configuración previa, y todas las demás dependen de ella. Actívela
  cuando el usuario instale el plugin, cuando pida configurarlo, o cuando otra skill se
  haya detenido por falta de configuración.
---

# Entrevista inicial — {DISPLAY}

## Qué produce

Dos archivos:

1. `{CFG}/perfil-organizacion.md` — compartido por todos los plugins. Si ya existe, no
   se repiten esas preguntas: se leen y se confirman en una sola pantalla.
2. `{CFG}/{SLUG}/CLAUDE.md` — el perfil de práctica de esta área, a partir de la
   plantilla que trae el plugin.

## Cómo se conduce

**Una pregunta a la vez.** No se lanzan diez preguntas en un bloque. Se pregunta, se
escucha, se repregunta si la respuesta quedó a medias, y se sigue. La entrevista dura
entre 10 y 15 minutos y produce un archivo que el usuario va a editar durante meses.

**Se puede pausar.** Si el usuario dice «después», se guarda lo que haya, se marca lo
que falta y se dice exactamente qué skills no van a funcionar hasta completar.

**No se inventan respuestas.** Si el usuario no sabe cuál es la posición de la casa
sobre algo, se deja `[PENDIENTE]` y se anota que esa skill va a preguntar cuando llegue
el caso. Un `[PENDIENTE]` honesto es mejor que un valor por defecto que nadie decidió.

## Banderas

- `--completa` — entrevista entera (por defecto en la primera ejecución).
- `--revisar-integraciones` — solo verifica qué conectores están respondiendo y
  actualiza esa tabla. Corre sin configuración previa.
- `--solo-criterios` — vuelve sobre la sección de criterios de la casa.

## Secuencia

### Bloque 0 — Antes de preguntar nada

Verificar si existe `{CFG}/perfil-organizacion.md`. Si existe, leerlo y mostrar un
resumen de tres líneas: «Ya tengo esto de su organización: [...]. ¿Sigue vigente?»
Si no existe, arrancar por el Bloque 1.

Verificar también si hay un `CLAUDE.md` diligenciado en la ruta antigua de caché del
plugin; si lo hay y no hay uno en la ruta de configuración, copiarlo antes de seguir.

### Bloque 1 — Quiénes son *(solo si no existe el perfil de organización)*

1. ¿Cómo se llama la organización y qué es? (firma, departamento jurídico, despacho
   individual, consultorio, entidad pública)
2. ¿Cuántas personas son en el equipo jurídico?
3. ¿En qué ciudades y circuitos actúan?
4. ¿Cuál es el sector o la industria?

### Bloque 2 — Quién va a usar esto

5. ¿Usted es abogado con tarjeta profesional vigente?
   - **Si sí:** registrar nombre y T.P. El encabezado de producto de trabajo será el de
     abogado.
   - **Si no:** preguntar si tiene abogado a quien consultar y quién es. El encabezado
     será el de notas de trabajo y **se activa la compuerta de revisión profesional en
     todas las skills**. Decirlo explícitamente ahora, no cuando ya esté por radicar.

6. ¿Es firma que representa clientes, área jurídica de una empresa, o ambas cosas?
   Esta respuesta cambia los encabezados, las compuertas y a quién se escala.

### Bloque 3 — Lo que duele

7. «¿Qué es lo que más tiempo le quita o más problemas le ha traído en {AMBITO_CORTO}?»
   Recoger la respuesta **en las palabras del usuario** y ponerla textual en el perfil.
   Esa frase es la que orienta qué skill se sugiere primero después.

### Bloque 4 — Criterios de la casa

Recorrer, una por una, las decisiones que este plugin necesita resueltas:

{BLOQUE_DEC}

Para cada una: ¿cuál es la posición estándar, cuál es la alternativa que aceptan, y
qué es lo que nunca aceptan? Si el usuario duda, ofrecer dos o tres opciones típicas
del mercado colombiano **marcadas como sugerencia**, no como estándar. Nunca escribir
una posición que el usuario no haya confirmado.

### Bloque 5 — Escalamiento

8. ¿Quién puede decidir qué, sin consultar?
9. ¿A quién se escala y por qué medio?
10. ¿Qué escala siempre, sin importar la cuantía?

### Bloque 6 — Integraciones

Recorrer y marcar ✓/✗:

{INTEG}

Para cada una que esté en ✗, decir en una línea qué se hace en su lugar. El usuario
debe salir de la entrevista sabiendo qué va a tener que hacer a mano.

### Bloque 7 — Estilo y salidas

11. ¿Cómo tratan al juez o a la autoridad en los escritos?
12. ¿Dónde queda el producto de trabajo?
13. ¿A dónde van las alertas de términos?
14. ¿Extensión típica de un concepto?

### Bloque 8 — Documentos semilla

15. «¿Tiene minutas, manuales, formatos o conceptos modelo de la casa? Si me los
    señala, los uso como referencia de estilo y de posiciones.»

Registrar cada uno en la tabla `## Documentos semilla revisados`. **No copiar su
contenido al perfil**: registrar la ruta y qué aporta.

### Bloque 9 — Verificación normativa

16. «La tabla de marco normativo de este plugin trae [N] normas. ¿Quiere que alguien
    del equipo verifique su vigencia y firme esa tabla? Es lo que después permite que
    las skills citen sin marca de duda.»

Registrar quién y cuándo en `**Estado de verificación de esta tabla:**`.

## Al cerrar

1. Escribir los dos archivos.
2. Mostrar un resumen de lo que quedó `[PENDIENTE]` y qué skill lo va a pedir.
3. Sugerir **una** skill concreta para empezar, elegida por lo que el usuario respondió
   en el Bloque 3.
4. Recordar en una línea: todo lo que salga de aquí es borrador para revisión
   profesional.

## Lo que esta skill NO hace

- No decide por el usuario las posiciones de la casa.
- No llena `[PENDIENTE]` con valores por defecto.
- No copia documentos del usuario al repositorio.
""", slug).replace("{DISPLAY}", p["display"]).replace("{BLOQUE_DEC}", bloque_dec)\
     .replace("{INTEG}", integ).replace("{AMBITO_CORTO}", p["ambito"].rstrip("."))


def skill_personalizar(p):
    return esc("""---
name: personalizar
description: >
  Ajusta el perfil de práctica de {DISPLAY} sin repetir la entrevista completa: cambiar
  una posición de la casa, un umbral de escalamiento, un destinatario de alertas, el
  estilo de los escritos o el estado de una integración. Actívela cuando el usuario diga
  que algo del perfil quedó mal, que cambió una política, o que quiere que las salidas
  se vean distinto.
---

# Personalizar — {DISPLAY}

## Qué hace

Edita `{CFG}/{SLUG}/CLAUDE.md` (y `{CFG}/perfil-organizacion.md` cuando el cambio es
de la organización y no del área) de forma quirúrgica.

## Cómo

1. **Leer antes de escribir.** Cargar el perfil actual y mostrar la sección que se va a
   tocar, tal como está hoy.
2. **Confirmar el cambio en una frase.** «Hoy dice X. ¿Lo cambio a Y?»
3. **Escribir solo esa sección.** No reescribir el archivo completo. No reformatear lo
   que no se pidió tocar.
4. **Decir qué skills quedan afectadas.** Un cambio de umbral de escalamiento cambia el
   comportamiento de varias skills; decir cuáles.

## Qué se puede cambiar

| Pedido típico | Sección que se toca |
|---|---|
| «Ese tope ya no es el nuestro» | `## Criterios de la casa` |
| «Ahora esto lo aprueba otra persona» | `## Escalamiento` |
| «Las alertas van a otro lado» | `## Estilo de la casa` |
| «Conectamos el gestor documental» | `## Integraciones disponibles` |
| «Los conceptos deben ser más cortos» | `## Estilo de la casa` |
| «Verificamos la tabla de normas» | `## Marco normativo de referencia` |
| «Queremos separar por casos» | `## Espacios de asunto` |
| «Somos más conservadores de lo que quedó» | `## Postura ante decisiones jurídicas discutibles` |

## Reglas

- **Nunca borrar una posición sin dejar constancia.** Si se reemplaza una posición de
  la casa, anotar la fecha del cambio al lado. El perfil es un documento que se audita.
- **Un `[PENDIENTE]` que se llena se llena con lo que dijo el usuario**, no con una
  redacción mejorada que cambie el sentido.
- **Si el cambio contradice derecho imperativo, decirlo.** El usuario puede fijar la
  política de la casa, pero no puede fijar que se acepte una cláusula nula. Ejemplo:
  «Puedo dejar registrada esa posición, pero tenga en cuenta que la condonación del dolo
  futuro no vale (CC art. 1522), así que la skill la va a marcar igual.»

## Si el perfil no existe

Decir: «Todavía no hay perfil que ajustar. ¿Corremos `/{SLUG}:entrevista-inicial`?»
""", p["slug"]).replace("{DISPLAY}", p["display"])


def skill_verificar(p):
    fuentes = "\n".join("- %s" % a for a in p["autoridades"])
    return esc("""---
name: verificar-citas
description: >
  Compuerta de verificación de fuentes para {DISPLAY}. Toma una pieza ya redactada —un
  concepto, una demanda, un memorando, un contrato, un boletín— y revisa una por una
  cada norma, sentencia, término y umbral citado, dejando explícito qué se confirmó
  contra fuente oficial y qué quedó marcado. Actívela antes de radicar, antes de enviar
  al cliente, o cuando el usuario pregunte si las citas están bien.
---

# Verificar citas — {DISPLAY}

> Esta es la skill que evita el problema más caro del uso de IA en Derecho: **la cita
> que parece correcta y no existe**. Nada sale de este plugin hacia una autoridad, un
> cliente o una contraparte sin pasar por aquí.

## Qué hace

1. **Extrae** toda cita de la pieza: leyes, artículos, decretos, sentencias,
   circulares, conceptos, términos, umbrales y cifras.
2. **Clasifica** cada una por el tipo de verificación que necesita.
3. **Verifica** lo que se pueda con las herramientas disponibles en la sesión.
4. **Marca** lo que no se pudo verificar, sin excepción.
5. **Entrega** una tabla de verificación y una versión de la pieza con las marcas
   puestas donde corresponde.

## Regla de oro

**Una cita solo se declara verificada si en esta sesión apareció en un resultado de una
fuente oficial.** No se asciende una cita porque suene bien, porque el modelo esté
seguro o porque «esa norma existe seguro». Ver `referencias/verificacion-de-fuentes.md`.

## Qué se verifica de cada tipo de cita

### Normas

| Punto | Pregunta |
|---|---|
| Existencia | ¿La ley/decreto con ese número y año existe? |
| Artículo | ¿El artículo citado dice lo que la pieza afirma? |
| Vigencia | ¿Está vigente? ¿Derogado expresa, orgánica o tácitamente? |
| Constitucionalidad | ¿Hay inexequibilidad total o parcial? ¿Exequibilidad **condicionada**? |
| Reglamentación | ¿Hay decreto reglamentario o circular que cambie su aplicación? |
| Compilación | ¿Está compilado en un decreto único? Citar el DUR además de la norma origen |

Fuente preferida: SUIN-Juriscol; en su defecto, Diario Oficial o la edición de la
Secretaría del Senado.

### Jurisprudencia

| Punto | Pregunta |
|---|---|
| Existencia | ¿La sentencia con esa nomenclatura existe? |
| Corporación y sala | ¿Es de la corporación que se dice? |
| Ratio | ¿Lo que se cita es la *ratio decidendi* o es *obiter dictum*? |
| Vigencia de la línea | ¿Hay sentencia de unificación o cambio de línea posterior? |
| M.P. y radicado | ¿Coinciden? Si no se tienen, **no se inventan** |

Ver `referencias/precedente-y-jurisprudencia.md`.

### Términos y caducidades

| Punto | Pregunta |
|---|---|
| Norma que lo fija | ¿Cuál artículo? |
| Hábiles o calendario | ¿Cuál de los dos? |
| Día de inicio | ¿Desde qué hecho corre y por qué? |
| Suspensión o interrupción | ¿Conciliación, reclamo escrito, recurso? |
| Calendario judicial | ¿Se descontó vacancia y días no hábiles? |

### Cifras y umbrales

SMLMV, UVT, cuantías de competencia, topes indemnizatorios, umbrales de obligados:
**siempre con el año**. Un SMLMV sin año es una cifra sin sentido. Ver
`referencias/valores-anuales.md`.

## Fuentes oficiales de esta área

{FUENTES}

Catálogo completo en `referencias/fuentes-oficiales.md`.

## Salida

```markdown
## Verificación de citas — [nombre de la pieza]

**Conector de investigación:** [respondió / no disponible]
**Citas encontradas:** [N] — **verificadas:** [N] — **marcadas:** [N]

| # | Cita | Tipo | Lo que afirma la pieza | Resultado | Fuente consultada |
|---|---|---|---|---|---|
| 1 | Ley 1564 de 2012, art. 90 | Norma | Inadmisión de la demanda | ✅ Confirmado | SUIN-Juriscol |
| 2 | C-836 de 2001 | Sentencia | Doctrina probable | ⚠️ No verificado | sin conector |
| 3 | 2 años de caducidad | Término | Reparación directa | ✅ Confirmado | CPACA art. 164 |
| 4 | 100 SMLMV | Umbral | Tope de perjuicio moral | ⚠️ Verificar unificación vigente | — |

### 🔴 No usar sin verificar
[Citas que sostienen una conclusión y no se pudieron confirmar. Estas bloquean la radicación.]

### 🟠 Verificar antes de enviar
[Citas accesorias sin confirmar.]

### ✏️ Correcciones propuestas
[Cita | lo que dice la pieza | lo que dice la fuente | texto corregido]

### Pieza marcada
[La pieza con las marcas insertadas donde corresponde.]
```

## Compuerta

Si hay al menos una cita en 🔴, cerrar con:

> Hay [N] cita(s) que sostienen conclusiones y no pude confirmar. **No radique ni envíe
> esta pieza hasta resolverlas.** Puedo (a) intentar de nuevo con otra fuente,
> (b) reformular el argumento sin esa cita, o (c) dejarlas marcadas para que las
> verifique usted. ¿Cuál prefiere?

## Bitácora

Toda cita confirmada se anota en `{CFG}/{SLUG}/bitacora-verificacion.md` para que la
siguiente pieza no la vuelva a verificar desde cero.

## Lo que esta skill NO hace

- No declara verificada una cita que no recuperó.
- No corrige el argumento jurídico: corrige la cita y señala si el argumento se cae.
- No sustituye la lectura del abogado.
""", p["slug"]).replace("{DISPLAY}", p["display"]).replace("{FUENTES}", fuentes)


def skill_asunto(p):
    return esc("""---
name: espacio-de-asunto
description: >
  Crea, cambia, lista y cierra espacios de asunto para {DISPLAY}, cuando se quiere que
  el contexto y las salidas queden aislados por caso o por cliente. Actívela cuando el
  usuario hable de trabajar «por casos», «por expedientes» o «por cliente», o cuando
  pida separar lo que hoy está mezclado.
---

# Espacio de asunto — {DISPLAY}

## Para qué

Por defecto, este plugin trabaja **a nivel de práctica**: un solo perfil, un solo
contexto, todas las salidas juntas. Eso le sirve a la mayoría de usuarios in-house.

Quien lleva casos de varios clientes necesita lo contrario: que el contexto de un caso
no se filtre a otro, que las salidas queden en la carpeta del caso, y que el conflicto
de interés no se vuelva un accidente de archivo.

## Estructura

```
{CFG}/{SLUG}/
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
| `/{SLUG}:espacio-de-asunto habilitar` | Enciende la maquinaria de asuntos y lo registra en el perfil |
| `/{SLUG}:espacio-de-asunto crear <slug>` | Crea el asunto y hace la entrevista corta de contexto |
| `/{SLUG}:espacio-de-asunto cambiar <slug>` | Fija el asunto activo |
| `/{SLUG}:espacio-de-asunto listar` | Lista los asuntos con su estado y su próximo término |
| `/{SLUG}:espacio-de-asunto cerrar <slug>` | Cierra el asunto y deja la nota de cierre |
| `/{SLUG}:espacio-de-asunto practica` | Vuelve a trabajar a nivel de práctica |

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
""", p["slug"]).replace("{DISPLAY}", p["display"])


# --------------------------------------------------------------------------
# Archivos de configuración del plugin
# --------------------------------------------------------------------------
def gen_mcp(p):
    servers = {}
    for k in p["mcp"]:
        titulo, url, desc = R.MCP[k]
        servers[titulo] = {"type": "http", "url": url, "title": titulo, "description": desc}
    cats = []
    for c in p["cats"]:
        for x in R.CATEGORIAS[c]:
            if x not in cats:
                cats.append(x)
    return {"mcpServers": servers, "recommendedCategories": cats}


GITIGNORE = """.DS_Store
*.log
# La configuración y los asuntos del usuario nunca entran al control de versiones
config/
asuntos/
expedientes/
bitacora-verificacion.md
"""


def main():
    for p in R.PLUGINS:
        slug = p["slug"]
        d = os.path.join(RAIZ, slug)
        json_escribir(os.path.join(d, ".claude-plugin", "plugin.json"), {
            "name": slug,
            "version": VERSION,
            "description": p["desc"],
            "author": dict(R.MARKETPLACE["author"]),
        })
        json_escribir(os.path.join(d, ".mcp.json"), gen_mcp(p))
        json_escribir(os.path.join(d, "hooks", "hooks.json"), {"hooks": {}})
        escribir(os.path.join(d, ".gitignore"), GITIGNORE)
        escribir(os.path.join(d, "CLAUDE.md"), gen_claude_md(p))
        escribir(os.path.join(d, "README.md"), gen_readme(p))
        escribir(os.path.join(d, "skills", "entrevista-inicial", "SKILL.md"), skill_entrevista(p))
        escribir(os.path.join(d, "skills", "personalizar", "SKILL.md"), skill_personalizar(p))
        escribir(os.path.join(d, "skills", "verificar-citas", "SKILL.md"), skill_verificar(p))
        escribir(os.path.join(d, "skills", "espacio-de-asunto", "SKILL.md"), skill_asunto(p))
        print("  ✓", slug)
    gen_marketplace()
    print("  ✓ .claude-plugin/marketplace.json (%d plugins)" % len(R.PLUGINS))


if __name__ == "__main__":
    print("Generando andamiaje común…")
    main()
