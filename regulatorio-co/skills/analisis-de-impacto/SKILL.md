---
name: analisis-de-impacto
description: >
  Toma una norma nueva y dice qué cambia en las obligaciones, en los contratos y en los
  procesos de la organización, con plan de adecuación y responsables. Actívela ante «cómo
  nos afecta esta norma», «análisis de impacto de la reforma», «qué tenemos que cambiar»,
  «adecuación normativa», «esta ley nos aplica?», «impacto de la sentencia».
---

# Análisis de impacto normativo

**Antes de empezar.** Leer el perfil. Y **conseguir el texto de la norma**: no se analiza
el impacto de una norma que solo se conoce por un titular o por un resumen de prensa.

## Paso 1 — Fijar la norma

| Punto | Qué se determina |
|---|---|
| **Identificación** | Tipo, número, fecha, publicación |
| **Jerarquía** | Ley estatutaria, orgánica, ordinaria, decreto con fuerza de ley, decreto reglamentario, resolución, circular, concepto. **Un concepto no crea obligaciones**; una circular externa de superintendencia a sus vigilados, sí |
| **Vigencia** | Desde cuándo. ¿Inmediata, diferida, gradual? |
| **Régimen de transición** | ¿Qué pasa con las situaciones en curso? |
| **Reglamentación** | ¿Requiere decreto o circular para ser aplicable? |
| **Qué deroga o modifica** | Expresa, orgánica o tácitamente |
| **Estado de constitucionalidad** | Demandas, condicionamientos, suspensiones provisionales |

Ver `referencias/jerarquia-normativa.md`.

**Si la norma requiere reglamentación y no la tiene, la mayor parte del impacto está
suspendido.** Decirlo primero: evita proyectos de adecuación prematuros.

## Paso 2 — El mapeo, obligación por obligación

Este es el trabajo central. Para cada obligación que la norma crea, modifica o elimina:

| Campo | Contenido |
|---|---|
| **Artículo** | |
| **Obligación** | En lenguaje operativo, no en lenguaje normativo |
| **¿Nos aplica?** | Con el criterio: sujeto obligado, umbral, actividad |
| **Situación actual** | Qué hacemos hoy |
| **Brecha** | Qué falta |
| **Qué hay que cambiar** | Documento, proceso, sistema, contrato, persona |
| **Área responsable** | |
| **Plazo legal** | |
| **Esfuerzo** | Alto / medio / bajo |
| **Riesgo de no hacerlo** | Sanción, nulidad, exposición contractual, reputacional |

**Regla de traducción:** «El responsable del tratamiento deberá adoptar medidas técnicas,
humanas y administrativas» no le sirve a nadie. «Hay que documentar quién tiene acceso a
la base de clientes y revisar los permisos cada seis meses» sí.

## Paso 3 — Los cuatro frentes que casi siempre se olvidan

| Frente | Pregunta |
|---|---|
| **Contratos vigentes** | ¿Hay cláusulas que quedan ilegales, ineficaces o desactualizadas? ¿Hay que renegociar? ¿Los contratos tienen cláusula de cambio normativo? |
| **Sistemas y datos** | ¿Hay que capturar información nueva, conservarla más tiempo, reportarla en otro formato? Estos cambios tienen tiempos de desarrollo que nadie considera |
| **Personas** | ¿Hay que crear un rol, capacitar, cambiar funciones? |
| **Terceros** | Proveedores, distribuidores, aliados: ¿su incumplimiento nos afecta? ¿Hay que trasladarles la obligación por contrato? |

**El frente de contratos es el que más sorpresas da.** Una norma que cambia un umbral
puede volver ineficaz una cláusula en trescientos contratos vigentes.

## Paso 4 — La oportunidad, no solo el riesgo

Un análisis de impacto que solo lista obligaciones nuevas está incompleto. También hay
que mirar:

- **Obligaciones que desaparecen** o se simplifican: hay procesos que se pueden dejar de
  hacer.
- **Ventajas competitivas**: si la norma es exigente y la organización ya cumple, eso es un
  argumento comercial.
- **Beneficios, incentivos o plazos de gracia** que la norma prevea.
- **Argumentos** que la norma da frente a contrapartes, autoridades o competidores.

## Paso 5 — El plan de adecuación

```
FASE 0 — Inmediato (antes de [fecha])
  [Lo que tiene plazo corriendo o riesgo alto]

FASE 1 — Corto plazo ([N] semanas)
  [Documentos, políticas, comunicaciones]

FASE 2 — Mediano plazo ([N] meses)
  [Procesos, sistemas, contratos]

FASE 3 — Sostenimiento
  [Monitoreo, capacitación periódica, auditoría]
```

Cada acción con **responsable con nombre**, **fecha** y **evidencia esperada**. Un plan
sin evidencia esperada no se puede auditar después.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Impacto — [norma]

### Resumen para decisión
**¿Nos aplica?** [SÍ / NO / PARCIALMENTE]
**Impacto general:** [🔴 alto / 🟠 medio / 🟡 bajo]
**Fecha límite más próxima:** [ ]
**Lo que hay que decidir esta semana:** [ ]

### La norma
| Punto | Contenido |
|---|---|
| Identificación y publicación | |
| Jerarquía y fuerza vinculante | |
| Vigencia | |
| Régimen de transición | |
| **Reglamentación pendiente** | |
| Qué deroga o modifica | |
| Estado de constitucionalidad | |

### Mapeo de obligaciones
| Art. | Obligación (en lenguaje operativo) | ¿Aplica? | Situación actual | Brecha | Responsable | Plazo | Riesgo |
|---|---|---|---|---|---|---|---|

### Frentes
| Frente | Impacto | Acción |
|---|---|---|
| Contratos vigentes | | |
| Sistemas y datos | | |
| Personas y roles | | |
| Terceros | | |

### Oportunidades
| Oportunidad | Cómo aprovecharla |
|---|---|

### Plan de adecuación
| Fase | Acción | Responsable | Fecha | Evidencia esperada |
|---|---|---|---|---|

### Exposición si no se hace nada
| Riesgo | Probabilidad | Impacto | Cuantificación |
|---|---|---|---|

### Puntos que requieren interpretación
| Punto | Lecturas posibles | Cuál se recomienda | Marca |
|---|---|---|---|
[con `[revisar]` para que decida el abogado responsable]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No analizar sobre resúmenes de prensa.** Se pide el texto.
- **Si falta reglamentación, decirlo primero.**
- **Distinguir lo que la norma exige de lo que sería buena práctica.** Mezclarlos infla el
  proyecto y le quita credibilidad al análisis.
- **Marcar los puntos de interpretación** en lugar de resolverlos en silencio.
- **Revisar siempre el frente de contratos vigentes.**

## Lo que esta skill NO hace

- No implementa el plan.
- No estima costos de desarrollo tecnológico.
- No sustituye el concepto del abogado responsable en los puntos marcados.
