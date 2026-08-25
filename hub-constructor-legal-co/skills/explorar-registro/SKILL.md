---
name: explorar-registro
description: >
  Busca skills jurídicas colombianas en los registros configurados y las resume con su
  procedencia, su frescura y sus señales de calidad. Actívela ante «busca una skill para»,
  «qué skills hay disponibles», «explorar el registro», «existe algo para derecho
  minero», «quiero ver qué hay de la comunidad».
---

# Explorar el registro

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/hub-constructor-legal-co/CLAUDE.md`:
**lista de registros permitidos** y quién autoriza agregar uno nuevo.

> **Encontrar no es instalar.** Esta skill explora y resume. La instalación pasa
> obligatoriamente por `/hub-constructor-legal-co:revisar-seguridad`.

## Paso 1 — Qué se está buscando, de verdad

Antes de buscar, precisar:

| Pregunta | Por qué |
|---|---|
| ¿Qué tarea concreta hay que resolver? | «Algo de laboral» no es una búsqueda |
| ¿Ya existe en este marketplace? | Revisar primero los 19 plugins propios evita instalar de más |
| ¿Es una necesidad recurrente o de una vez? | Para lo de una vez, casi nunca vale la pena instalar nada |
| ¿Qué datos tendría que tocar? | Define el nivel de escrutinio de seguridad |
| ¿Quién la va a usar? | |

**El resultado más frecuente de esta skill debería ser «no hace falta instalar nada».**
Un entorno con veinte skills instaladas y tres en uso es un entorno con diecisiete
superficies de riesgo sin beneficio.

## Paso 2 — Dónde se busca

| Registro | Contenido | Confianza base |
|---|---|---|
| **Este marketplace** | Los 19 plugins de `claude-legal-colombia` | Alta — es el propio |
| **Marketplaces oficiales de Anthropic** | Plugins publicados por el proveedor | Alta |
| **Repositorios de firmas o universidades colombianas identificadas** | | Media — depende del autor |
| **Repositorios comunitarios** | | **Baja — escrutinio máximo** |
| **Registros no incluidos en la lista del perfil** | | **No se exploran sin autorización** |

## Paso 3 — Las señales que se recogen de cada candidata

| Señal | Qué mirar | Bandera roja |
|---|---|---|
| **Autor identificable** | Persona u organización real, con historia | Autor anónimo o creado la semana pasada |
| **Jurisdicción** | ¿Es de derecho colombiano o es una traducción de otro sistema? | Skills «traducidas» que citan doctrina extranjera como si fuera aplicable |
| **Frescura** | Última actualización | Sin actualizar desde antes de la última reforma de la materia |
| **Contenido normativo** | ¿Cita normas vigentes? ¿Con artículo? | Normas derogadas; citas sin artículo |
| **Manejo de citas** | ¿Marca lo que no verificó? | **Skills que afirman jurisprudencia sin marca de verificación: es la bandera roja más grave** |
| **Permisos y herramientas** | Qué pide en el frontmatter | Herramientas de red o de escritura sin justificación |
| **Servidores MCP** | A dónde se conecta | URLs desconocidas |
| **Manejo de datos** | ¿Dice qué hace con la información? | Silencio total sobre datos |
| **Compuertas** | ¿Tiene revisión profesional, control de términos? | Skills que generan piezas listas para radicar sin compuerta |
| **Licencia** | | Sin licencia |
| **Actividad** | Issues, correcciones, respuesta del autor | Repositorio abandonado |

## Paso 4 — El resumen que se entrega

Para cada candidata, lo suficiente para decidir si vale la pena la revisión de seguridad
—que cuesta tiempo—:

```markdown
### [Nombre de la skill] — [autor]

**Qué hace:** [una frase]
**Origen:** [registro] · **Última actualización:** [fecha] · **Licencia:** [ ]
**Jurisdicción declarada:** [Colombia / otra / no declarada]

| Señal | Estado |
|---|---|
| Autor identificable | |
| Normas citadas vigentes | |
| Marca las citas no verificadas | |
| Compuerta de revisión profesional | |
| Herramientas que solicita | |
| Servidores MCP a los que se conecta | |
| Manejo de datos declarado | |

**Banderas rojas:** [ ]
**Cubre lo que buscamos:** [totalmente / parcialmente — qué falta]
**¿Ya lo hace un plugin propio?** [cuál]
**Recomendación:** [pasar a revisión de seguridad / descartar — por qué / construirla
nosotros]
```

## Paso 5 — La alternativa que casi siempre gana

Antes de instalar algo de un tercero, comparar honestamente:

| Opción | Costo | Riesgo | Control |
|---|---|---|---|
| **Instalar la de la comunidad** | Bajo | **Alto**: código y prompts de terceros con acceso al entorno | Ninguno |
| **Construirla con `/hub-constructor-legal-co:crear-skill-juridica`** | Medio | Bajo | Total |
| **Adaptar una skill propia existente** | Bajo | Bajo | Total |
| **No hacer nada** | Cero | Cero | — |

**Para skills jurídicas, construir suele ganar.** El contenido normativo tiene que estar
verificado de todos modos, y verificar el de otro cuesta casi lo mismo que escribir el
propio con las convenciones de la casa.

## Salida

```markdown
[NOTAS DE TRABAJO]

## Exploración — [necesidad]

### Lo que se buscaba
### ¿Ya existe en el marketplace propio?
| Plugin | Skill | ¿Cubre la necesidad? |
|---|---|---|

### Candidatas encontradas
[el resumen por candidata]

### Comparación
| Opción | Costo | Riesgo | Control | Recomendación |
|---|---|---|---|---|

### Recomendación
[ ]

### Si se decide avanzar
Siguiente paso obligatorio: `/hub-constructor-legal-co:revisar-seguridad`
```

## Compuertas

- **No se exploran registros fuera de la lista del perfil** sin autorización.
- **Encontrar no es recomendar instalar.**
- **Toda candidata sin marca de verificación de citas se descarta o se marca como riesgo
  alto.** En derecho, una skill que afirma jurisprudencia sin verificar es peligrosa por
  diseño.
- **Revisar siempre si un plugin propio ya lo hace.**

## Lo que esta skill NO hace

- No instala.
- No ejecuta código de las candidatas.
- No garantiza que una skill sea segura por estar en un registro conocido.
