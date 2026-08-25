---
name: control-de-calidad
description: >
  Audita las skills instaladas contra la lista de calidad del repositorio: citas,
  términos, compuertas, actualidad normativa y uso real. Actívela ante «auditoría de
  skills», «revisar las skills instaladas», «control de calidad del entorno», «hace cuánto
  no revisamos esto», «esta skill está dando resultados raros», «limpieza del entorno».
---

# Control de calidad

> **Una skill jurídica se degrada sola.** Las normas cambian, la jurisprudencia se unifica,
> los umbrales se actualizan cada año. Una skill que era correcta hace dieciocho meses
> puede estar citando una norma derogada hoy, y nadie se entera hasta que sale en un
> memorial.

**Antes de empezar.** Leer el perfil: periodicidad de la auditoría y quién la aprueba.

## Periodicidad

| Disparador | Alcance |
|---|---|
| **Auditoría periódica** | Semestral, todas las skills instaladas |
| **Reforma normativa material** | Solo las skills del área afectada, de inmediato |
| **Sentencia de unificación** | Las skills que dependen de la línea |
| **Cambio de año** | Todas las que usen SMLMV, UVT o umbrales anuales — **enero, sin excepción** |
| **Comportamiento anómalo reportado** | La skill señalada, de inmediato |
| **Actualización de una skill de terceros** | Esa skill, con revisión de seguridad si cambió el alcance |

**El barrido de enero es el más importante y el más olvidado:** todo lo que esté en SMLMV
o UVT quedó desactualizado el 1.º de enero.

## La lista de calidad

Cada skill se audita contra estos quince puntos:

### Contenido jurídico

| # | Verificación | Cómo se comprueba |
|---|---|---|
| 1 | **Normas vigentes** | Contrastar cada norma citada contra SUIN-Juriscol |
| 2 | **Artículos correctos** | ¿El artículo dice lo que la skill afirma? |
| 3 | **Sin normas derogadas** | Especial atención tras reformas |
| 4 | **Condicionamientos incorporados** | Exequibilidades condicionadas que cambian la aplicación |
| 5 | **Jurisprudencia vigente** | ¿Hay unificación posterior? |
| 6 | **Umbrales con año** | SMLMV, UVT, cuantías, topes |
| 7 | **Términos con norma** | Y con advertencia de calendario judicial |

### Convenciones del repositorio

| # | Verificación |
|---|---|
| 8 | Etiquetas de procedencia en las citas |
| 9 | Encabezado de producto de trabajo |
| 10 | Nota al revisor en las salidas |
| 11 | Compuerta de revisión profesional |
| 12 | Manejo de datos personales |
| 13 | Sección «Lo que esta skill NO hace» |

### Funcionamiento

| # | Verificación |
|---|---|
| 14 | **Referencias a otras skills que existen** — el validador lo comprueba |
| 15 | **Uso real**: ¿alguien la usa? |

## El punto 15: la skill que nadie usa

Una skill sin uso en seis meses es **superficie de riesgo sin beneficio**. Preguntas:

- ¿No se usa porque no hace falta? → **Desinstalar.**
- ¿No se usa porque no se dispara? → Arreglar la descripción.
- ¿No se usa porque nadie sabe que existe? → Comunicar.
- ¿No se usa porque da malos resultados? → Arreglar o desinstalar.

**La respuesta más común es la segunda**, y se arregla con veinte minutos de trabajo en el
campo `description`.

## Las señales de degradación

| Señal | Qué indica |
|---|---|
| La skill cita una norma que se reformó | Contenido desactualizado |
| Sus salidas traen citas sin marca | Se perdió la disciplina de verificación |
| Los usuarios corrigen siempre lo mismo | Hay un error sistemático |
| Produce salidas más largas de lo útil | Hay que podarla |
| Se dispara en casos que no le corresponden | Descripción demasiado amplia |
| No se dispara cuando debería | Descripción demasiado estrecha |
| Nadie la usa | Ver arriba |

**Preguntarles a los usuarios qué corrigen siempre** es el diagnóstico más eficiente y el
que menos se hace.

## La auditoría de una skill de terceros

Además de todo lo anterior:

| Verificación |
|---|
| ¿El autor sigue manteniéndola? |
| ¿Cambió su contenido desde la última revisión? |
| ¿Pide permisos nuevos? |
| ¿Se conecta a destinos nuevos? |
| **¿Sigue justificándose frente a una alternativa propia?** |

**Si el contenido cambió, se vuelve a
`/hub-constructor-legal-co:revisar-seguridad`.** Una actualización puede introducir
exactamente lo que la revisión inicial descartó.

## Salida

```markdown
[NOTAS DE TRABAJO]

## Control de calidad — [fecha] — [periódica / disparada por (evento)]

### Resumen
| Métrica | Valor |
|---|---|
| Skills auditadas | |
| ✅ Sin hallazgos | |
| ⚠️ Con hallazgos menores | |
| 🔴 Con hallazgos críticos | |
| Propuestas para desinstalar | |

### 🔴 Hallazgos críticos
| Skill | Hallazgo | Riesgo | Acción | Responsable | Plazo |
|---|---|---|---|---|---|
[p. ej.: «cita el artículo X de la Ley Y, derogado por la reforma Z: cualquier salida que
lo invoque es incorrecta»]

### Auditoría por skill
| Skill | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | Veredicto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### Barrido de valores anuales
| Skill | Umbral que usa | Año registrado | Año vigente | Estado |
|---|---|---|---|---|

### Skills sin uso
| Skill | Última vez usada | Diagnóstico | Recomendación |
|---|---|---|---|

### Skills de terceros
| Skill | ¿Cambió? | ¿Requiere nueva revisión de seguridad? | ¿Sigue justificándose? |
|---|---|---|---|

### Retroalimentación de usuarios
| Skill | Qué corrigen siempre | Qué hay que arreglar |
|---|---|---|

### Plan de remediación
| Acción | Skill | Responsable | Plazo |
|---|---|---|---|

### Próxima auditoría
[fecha] — **Disparadores anticipados:** [reformas en trámite que la activarían]
```

## Compuertas

- **Una skill con norma derogada o con jurisprudencia superada se marca 🔴 y se corrige o
  se deshabilita.** No se deja «para después»: sigue produciendo salidas.
- **El barrido de valores anuales se hace en enero**, sin esperar la auditoría semestral.
- **Si una skill de terceros cambió, vuelve a revisión de seguridad.**
- **Una skill sin uso se desinstala o se arregla; no se deja instalada por si acaso.**
- **La auditoría queda por escrito, con fecha y responsable.**

## Lo que esta skill NO hace

- No corrige las skills: identifica y propone.
- No verifica la vigencia normativa por sí sola: define qué hay que verificar y dónde.
- No desinstala.
