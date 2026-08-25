---
name: crear-skill-juridica
description: >
  Crea una skill jurídica nueva con las convenciones de este repositorio: frontmatter que
  dispara bien, verificación de fuentes, control de términos, compuertas de revisión
  profesional y salidas accionables. Actívela ante «crear una skill», «hacer una skill
  para mi área», «cómo escribo una skill jurídica», «quiero automatizar este
  procedimiento», «adaptar una skill a mi práctica».
---

# Crear una skill jurídica

**Antes de empezar.** Leer el perfil y el `CLAUDE.md` de la raíz del repositorio, que trae
las convenciones. Y una decisión previa: **¿hace falta una skill nueva?** Si un plugin
propio ya cubre el 80%, casi siempre conviene extender el existente.

## Paso 1 — El diseño, antes de escribir

| Pregunta | Por qué |
|---|---|
| **¿Qué tarea concreta resuelve?** | Una skill, una tarea. Si necesita «y» para describirla, son dos skills |
| **¿Quién la va a usar?** | Abogado, dependiente, personal no jurídico. Cambia las compuertas |
| **¿Qué información necesita para funcionar?** | Lo que hay que pedirle al usuario |
| **¿Qué produce?** | Un entregable concreto, no «un análisis» |
| **¿Qué puede salir mal?** | Aquí nacen las compuertas |
| **¿Qué términos toca?** | Si toca alguno, hay que controlarlo |
| **¿Toca datos personales?** | |
| **¿Produce una pieza que sale del despacho?** | Si sí, necesita verificación de citas y nota al revisor |

**La pregunta 5 es la que distingue una skill jurídica útil de una plantilla.** El valor
está en las compuertas, no en el formato.

## Paso 2 — El frontmatter, que decide si la skill se usa

```yaml
---
name: nombre-en-kebab-case
description: >
  Qué hace, en una frase. Y cuándo debe activarse, con **las frases que el usuario diría
  de verdad**: «me llegó una demanda», «cuánto le debo a este trabajador», «¿puedo firmar
  esto?». Este campo es lo que decide si la skill se dispara; escríbalo pensando en el
  disparo, no en el resumen.
---
```

| Regla | Razón |
|---|---|
| **`name` igual al nombre del directorio** | El validador lo comprueba |
| **La descripción trae frases de disparo reales** | Nadie escribe «requiero efectuar un análisis de viabilidad»; escribe «¿vale la pena demandar?» |
| **Incluir sinónimos y coloquialismos** | «Despido», «me echaron», «terminación del contrato» |
| **Decir la jurisdicción** cuando importa | «en Colombia» |
| **No prometer lo que la skill no hace** | Una descripción inflada dispara la skill en casos que no resuelve |

## Paso 3 — La estructura del cuerpo

```markdown
# Título

> [Advertencia dominante, si la hay: el riesgo que define esta skill]

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/<plugin>/CLAUDE.md`.
[Qué se detiene si falta configuración. Qué skill se corre antes.]

## [Paso 0 — 🔴 Lo urgente, si aplica]
[Términos, riesgo para personas, caducidad. Si la skill toca algo con reloj, va primero.]

## Marco normativo
[Tabla: norma | qué gobierna. Con artículo. Con advertencia de verificación.]

## Cómo se hace
[Los pasos, con tablas de decisión. Denso, sin relleno.]

## Salida
[Plantilla en bloque de código, con encabezado de producto de trabajo, tablas y nota al
revisor.]

## Compuertas
[Qué detiene la skill. Qué no se hace aunque lo pidan.]

## Lo que esta skill NO hace
[Límites explícitos. Evita que se use para lo que no sirve.]
```

## Paso 4 — Las convenciones que no son opcionales

Estas hacen que la skill pertenezca a este repositorio y no sea una plantilla más:

| # | Convención | Cómo se ve |
|---|---|---|
| 1 | **Verificación de fuentes** | Toda cita etiquetada; `[conocimiento del modelo — verificar]` por defecto |
| 2 | **Términos con norma** | Nunca un número suelto: artículo, hábiles o calendario, día de inicio, advertencia de calendario judicial |
| 3 | **Encabezado de producto de trabajo** | Según el rol configurado |
| 4 | **Nota al revisor** | `Fuentes: … \| Marcas pendientes: … \| Revisó: …` |
| 5 | **Compuerta de revisión profesional** | Si el rol no es abogado inscrito |
| 6 | **Datos personales** | Anonimizar antes de procesar |
| 7 | **Verificación de destinatario** | Antes de que una pieza salga |
| 8 | **Piso de severidad** | Un hallazgo 🔴 no se degrada en silencio |
| 9 | **Derecho imperativo sobre criterios de la casa** | La política del cliente no autoriza lo que la ley prohíbe |
| 10 | **Referencias compartidas** | Remitir a `referencias/` en vez de copiar |

## Paso 5 — Las reglas de redacción

| Regla | Razón |
|---|---|
| **Densidad sobre volumen** | 120 líneas útiles vencen a 400 que repiten guardarraíles |
| **Tablas para decisiones** | Un árbol de decisión en prosa no se sigue |
| **Segunda persona o impersonal, no primera** | «Se verifica», «verifique» |
| **Ejemplos reales del oficio** | «El arrendatario no consignó y no fue oído» enseña más que una regla abstracta |
| **Decir lo incómodo** | «Si su cliente incumplió primero, dígaselo antes que nada» |
| **Marcar lo que no se sabe** | `[verificar]` es una respuesta profesional |
| **Nombres de skill reales** | Si dice «corra `/foo`», `foo` debe existir. El validador lo comprueba |
| **Artículos, no solo leyes** | «Ley 1564 de 2012, art. 90», no «el CGP» |
| **Umbrales con año** | Todo SMLMV y toda UVT con su año |

## Paso 6 — La prueba

Antes de dar por terminada la skill:

| # | Prueba |
|---|---|
| 1 | **Disparo:** escribir tres frases que un usuario diría. ¿La skill se activaría? |
| 2 | **Caso completo:** correrla con un caso realista. ¿La salida sirve? |
| 3 | **Caso incompleto:** correrla sin información suficiente. ¿Pregunta o inventa? |
| 4 | **Caso fuera de alcance:** ¿lo detecta y lo dice? |
| 5 | **Compuertas:** ¿se activan cuando deben? |
| 6 | **Citas:** ¿todas etiquetadas? |
| 7 | **Validador:** `python3 scripts/validar.py` en 0 errores |

**La prueba 3 es la más importante.** Una skill que inventa cuando le falta información es
peor que ninguna skill.

## Paso 7 — Dónde va

```
<plugin>/skills/<nombre-en-kebab>/SKILL.md
```

Y si es una skill propia del repositorio, hay que **registrarla en
`scripts/registro.py`** (lista `propias` del plugin) y regenerar, para que aparezca en el
README del plugin. Ver el `CLAUDE.md` de la raíz.

## Salida

```markdown
[NOTAS DE TRABAJO]

## Skill nueva — [nombre]

### Diseño
| Pregunta | Respuesta |
|---|---|
| Tarea que resuelve | |
| Usuario | |
| Entradas | |
| Entregable | |
| **Qué puede salir mal** | |
| Términos que toca | |
| Datos personales | |
| ¿Produce pieza que sale del despacho? | |

### ¿Ya existe algo parecido?
| Plugin | Skill | ¿Se puede extender en vez de crear? |
|---|---|---|

---
[SKILL.md COMPLETA]
---

### Convenciones aplicadas
| # | Convención | ¿Aplicada? |
|---|---|---|

### Pruebas
| # | Prueba | Resultado |
|---|---|---|

### Para integrarla al repositorio
1. Guardar en `<plugin>/skills/<nombre>/SKILL.md`
2. Registrar en `scripts/registro.py`
3. `python3 scripts/generar-comunes.py`
4. `python3 scripts/validar.py` → debe salir en 0 errores
```

## Compuertas

- **No crear una skill que produzca piezas listas para radicar sin compuerta de revisión
  profesional.**
- **No crear una skill que cite jurisprudencia sin marca de verificación.**
- **No crear una skill que calcule términos sin la norma y la advertencia de calendario.**
- **Si ya existe algo que cubre el 80%, recomendar extenderlo.**

## Lo que esta skill NO hace

- No publica ni distribuye la skill.
- No garantiza que el contenido jurídico sea correcto: eso lo verifica un abogado.
- No sustituye la prueba con casos reales.
