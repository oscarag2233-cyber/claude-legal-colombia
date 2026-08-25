---
name: vigilancia-normativa
description: >
  Barrido periódico de fuentes oficiales colombianas con filtro de materialidad, para que
  el equipo lea diez líneas y no doscientas. Actívela ante «qué salió esta semana»,
  «vigilancia normativa», «monitoreo regulatorio», «novedades normativas», «qué publicó la
  Superintendencia», «revisa el Diario Oficial», o para configurar el barrido periódico.
---

# Vigilancia normativa

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/regulatorio-co/CLAUDE.md`,
especialmente las fuentes y la periodicidad configuradas, y el **criterio de materialidad**
de la casa.

> **El problema de la vigilancia normativa no es encontrar novedades: es descartarlas.**
> Un boletín con cuarenta ítems no lo lee nadie. Uno con cuatro, bien escogidos, cambia
> decisiones.

## Paso 1 — Las fuentes

| Fuente | Qué trae | Periodicidad natural |
|---|---|---|
| **Diario Oficial** | Leyes, decretos, resoluciones; la publicación que da vigencia | Diaria |
| **SUIN-Juriscol** | Texto normativo con historial de vigencia y notas de derogatoria e inexequibilidad | Consulta |
| **Corte Constitucional — relatoría y comunicados de prensa** | Sentencias C, SU y T. **Los comunicados salen antes que el texto completo** | Semanal |
| **Corte Suprema — relatorías** | Salas Civil, Laboral y Penal | Semanal |
| **Consejo de Estado — relatoría** | Secciones; **sentencias de unificación** | Semanal |
| **Superintendencias** (SIC, Sociedades, Financiera, Salud, Servicios Públicos, Transporte, Vigilancia) | Circulares externas, resoluciones, conceptos | Semanal |
| **DIAN** | Resoluciones, conceptos, calendario | Semanal |
| **Ministerios y unidades administrativas** | Decretos reglamentarios, resoluciones | Semanal |
| **Proyectos en consulta pública** | Sitios de las entidades — ventana para comentar | Semanal |
| **Congreso** | Proyectos de ley en trámite; gaceta del Congreso | Quincenal |
| **Colombia Compra Eficiente** | Documentos tipo, circulares | Mensual |
| **Comunidad Andina** | Decisiones y resoluciones | Mensual |

Ver `referencias/fuentes-oficiales.md` para el catálogo completo.

**Advertencia operativa:** si no hay conectores configurados, la recolección la hace el
usuario y esta skill **procesa y filtra** lo que él aporte. Decirlo en la salida en lugar
de simular una recolección que no ocurrió.

## Paso 2 — El filtro de materialidad

Cada novedad pasa por cuatro preguntas, en este orden. **Basta que una falle para que no
entre al boletín**:

| # | Pregunta | Si la respuesta es no |
|---|---|---|
| 1 | **¿Nos aplica?** ¿Toca una actividad, un sector o una obligación de la organización o de sus clientes? | Se descarta |
| 2 | **¿Cambia algo?** ¿Modifica una obligación, un plazo, un umbral, un procedimiento o una interpretación vigente? | Se descarta (una norma que reitera lo existente no es noticia) |
| 3 | **¿Exige acción?** ¿Hay que hacer algo, y para cuándo? | Baja a «para conocimiento» |
| 4 | **¿Alguien tiene que decidir?** | Sube de prioridad |

**Clasificación resultante:**

| Nivel | Criterio |
|---|---|
| 🔴 **Acción inmediata** | Hay plazo corriendo, o entra en vigencia pronto, o hay que ajustar algo antes de una fecha |
| 🟠 **Requiere análisis** | Impacta, pero hay que estudiar cómo. Se asigna responsable |
| 🟡 **Para conocimiento** | Relevante, sin acción inmediata |
| ⚪ **Descartado** | Se registra que se miró y se descartó, **con la razón** |

**Registrar los descartes** es lo que permite defender el barrido: «no se revisó» y «se
revisó y no aplica» son cosas distintas cuando alguien pregunta seis meses después.

## Paso 3 — Qué se mira de cada novedad

| Elemento | Por qué |
|---|---|
| **Tipo de norma** | Ley, decreto, resolución, circular, concepto, sentencia. Determina su fuerza |
| **Número, fecha y publicación** | Identificación verificable |
| **Entrada en vigencia** | Inmediata, diferida, gradual, sujeta a reglamentación |
| **Qué deroga o modifica** | Aquí está el cambio real |
| **A quién aplica** | Sujetos obligados, umbrales |
| **Qué obligación crea o modifica** | En una frase accionable |
| **Plazos** | Los que corren desde ya |
| **Reglamentación pendiente** | Si la norma no se puede aplicar sin decreto o circular posterior, decirlo |
| **Estado de constitucionalidad** | Demandas en curso, condicionamientos |

**Sentencias:** distinguir el **comunicado de prensa** del **texto completo**. El
comunicado permite alertar temprano, pero **la regla vinculante está en la *ratio* del
texto**, que puede tardar semanas. Marcarlo: `[comunicado — texto pendiente]`.

## Paso 4 — La escritura

Cada ítem se escribe para alguien que tiene treinta segundos:

```
🔴 **[Tipo y número] — [titular en una línea, en lenguaje de negocio]**
Qué cambia: [una o dos frases]
A quién aplica: [ ]
Desde cuándo: [fecha o «sujeto a reglamentación»]
Qué hay que hacer: [acción concreta] — Responsable: [ ] — Antes de: [fecha]
Fuente: [Diario Oficial n.º / relatoría] `[etiqueta de verificación]`
```

**Reglas de redacción:**

- **El titular dice el efecto, no el nombre de la norma.** «Nuevo plazo para reportar
  incidentes de datos: 10 días» sirve; «Circular Externa 003 de 2026 de la SIC» no.
- **Sin transcripciones.** Si hay que citar, una frase.
- **Nunca un ítem sin «qué hay que hacer»**, aunque sea «nada por ahora».
- **Toda cita etiquetada** conforme a `referencias/verificacion-de-fuentes.md`.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Vigilancia normativa — [período]

**Fuentes revisadas:** [lista] — **Recolección:** [conector / aportada por el usuario]
**Ítems revisados:** [N] — **Materiales:** [N] — **Descartados:** [N]

### 🔴 Acción inmediata
[ítems con el formato de arriba]

### 🟠 Requiere análisis
| Novedad | Impacto probable | Quién analiza | Para cuándo |
|---|---|---|---|

### 🟡 Para conocimiento
| Novedad | Qué es | Por qué se menciona |
|---|---|---|

### ⚪ Revisados y descartados
| Novedad | Razón del descarte |
|---|---|

### En trámite — vigilancia
| Proyecto / demanda | Estado | Qué pasaría si prospera | Próximo hito |
|---|---|---|---|

### Reglamentación pendiente
| Norma | Qué falta reglamentar | Impacto de la demora |
|---|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No reportar una novedad sin verificar su publicación oficial.** Los medios y las redes
  publican proyectos como si fueran normas aprobadas.
- **Distinguir proyecto de norma vigente**, y comunicado de sentencia.
- **Marcar la reglamentación pendiente:** una norma que no se puede aplicar todavía no
  genera obligación hoy, y decir lo contrario provoca trabajo inútil.
- **Registrar los descartes con su razón.**
- **Si no hubo recolección automatizada, decirlo:** el alcance del barrido es el de lo que
  efectivamente se revisó.

## Lo que esta skill NO hace

- No consulta fuentes si no hay conectores: procesa lo que se le aporte.
- No analiza el impacto en profundidad — para eso está
  `/regulatorio-co:analisis-de-impacto`.
- No sustituye la lectura del texto normativo por el abogado responsable.
