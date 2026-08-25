---
name: boletin-normativo
description: >
  Arma el boletín periódico con las novedades priorizadas y una acción concreta por cada
  una, en el formato que el equipo efectivamente lee. Actívela ante «arma el boletín»,
  «newsletter jurídico», «resumen normativo de la semana», «alerta para clientes», «el
  digest del lunes», «boletín para la junta».
---

# Boletín normativo

**Antes de empezar.** Leer el perfil: destinatarios, formato y periodicidad. Y correr
`/regulatorio-co:vigilancia-normativa` para tener los insumos filtrados.

> **El boletín compite con el correo de todo el mundo.** Si no se puede leer en dos
> minutos, no se lee. Y un boletín que no se lee es peor que ninguno: da la sensación de
> que el equipo está informado cuando no lo está.

## Paso 1 — Para quién

El mismo insumo produce boletines distintos:

| Destinatario | Qué le importa | Extensión | Tono |
|---|---|---|---|
| **Junta o alta dirección** | Riesgo, plata, decisiones. Solo lo que cambia el rumbo | 1 pantalla, 3-5 ítems | Ejecutivo, sin normas en el cuerpo |
| **Equipo jurídico** | Todo lo material, con la cita exacta | 1-2 páginas | Técnico |
| **Áreas operativas** | Qué tienen que hacer distinto desde el lunes | Corto y por área | Operativo, sin jerga |
| **Clientes de la firma** | Qué les afecta, con el sello de la firma | 1 página | Profesional, con oferta de acompañamiento |
| **Gremio** | Posición del sector, oportunidades de incidencia | | |

**Si hay varios destinatarios, hacer versiones**, no un boletín largo que sirva para
todos. El boletín para todos no sirve para nadie.

## Paso 2 — La estructura

```markdown
# [Nombre del boletín] — [período]

## En una línea
[La novedad más importante del período, y qué implica. Si alguien solo lee esto, que se
lleve lo esencial.]

---

## 🔴 Acción requerida

### [Titular en lenguaje de negocio]
**Qué pasó:** [1-2 frases]
**A quién aplica:** [ ]
**Desde cuándo:** [fecha]
**Qué hay que hacer:** [acción concreta] — **Responsable:** [ ] — **Antes de:** [fecha]
*[Norma] · [fuente]* `[etiqueta]`

---

## 🟠 Para analizar
| Novedad | Qué implicaría | Quién lo mira | Para cuándo |
|---|---|---|---|

---

## 🟡 Para conocer
- **[Titular]** — [una línea]. *[Norma]*

---

## 👀 En el radar
| Qué | Estado | Cuándo se define | Si prospera |
|---|---|---|---|
[proyectos de ley, demandas de inconstitucionalidad, reglamentaciones pendientes]

---

## 📅 Vencimientos del mes
| Obligación | Fecha | Responsable |
|---|---|---|

---
*Este boletín es informativo y no constituye asesoría jurídica. Las normas citadas deben
verificarse en su fuente oficial antes de tomar decisiones. Preparado por [ ] el [fecha].*
```

## Paso 3 — Las reglas de escritura

| Regla | Ejemplo |
|---|---|
| **El titular dice el efecto, no el nombre de la norma** | ❌ «Circular Externa 005 de 2026 de la SIC» → ✅ «El plazo para responder reclamos de titulares baja a 10 días» |
| **Verbo al principio de la acción** | «Actualizar la política antes del 30 de junio» |
| **Sin transcripciones** | Una frase citada como máximo |
| **Sin latinismos ni jerga** | «Prima facie», «sin perjuicio de», «ope legis» no van |
| **Cada ítem con acción**, aunque sea «ninguna por ahora» | |
| **Fechas, no plazos relativos** | «Antes del 15 de mayo», no «en dos meses» |
| **Máximo 5 ítems en 🔴** | Si hay más, el período fue excepcional y hay que decirlo |
| **Toda cita etiquetada** | `[Diario Oficial]`, `[conocimiento del modelo — verificar]` |

## Paso 4 — El aviso legal

Todo boletín que sale de la organización lleva aviso. Y **la verificación de destinatario**
del perfil: un boletín para clientes es comunicación externa y no está amparado por la
reserva profesional.

Si el boletín va a clientes de una firma, revisar además:
- Que no constituya asesoría específica para un caso concreto.
- Que no genere expectativa de acompañamiento no contratado.
- Que las citas estén verificadas: **un boletín es la carta de presentación técnica de la
  firma, y una cita equivocada ahí es cara.**

## Paso 5 — La mejora continua

| Métrica | Para qué |
|---|---|
| ¿Cuántos ítems generaron acción efectiva? | Si es cero durante tres períodos, el filtro de materialidad está mal calibrado |
| ¿Qué preguntan los destinatarios después de leerlo? | Lo que preguntan es lo que faltó explicar |
| ¿Qué novedad los tomó por sorpresa después? | Falla del barrido: hay que ajustar fuentes |
| ¿Se lee? | Preguntar directamente cada cierto tiempo |

## Salida

El boletín, listo para enviar, más:

```markdown
### Nota interna
**Destinatario de esta versión:** [ ]
**Ítems revisados en el período:** [N] — **incluidos:** [N] — **descartados:** [N]
**Citas verificadas en fuente oficial:** [N] de [N]
**Marcas pendientes:** [ítems que salen con `[verificar]` y por qué]
**Versiones adicionales sugeridas:** [para junta / para operaciones / para clientes]

Fuentes: […] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Ninguna cita sin verificar en un boletín que sale de la organización.** Es el
  documento más público que produce el área jurídica.
- **Verificación de destinatario** antes de generar.
- **No incluir asesoría específica de un caso** en un boletín general.
- **Si un período no tiene nada material, decirlo:** «Sin novedades materiales en el
  período» es una entrega válida y mantiene la credibilidad del filtro.
- **Distinguir proyecto de norma vigente** en el radar.

## Lo que esta skill NO hace

- No envía el boletín.
- No hace la vigilancia — para eso está `/regulatorio-co:vigilancia-normativa`.
- No sustituye el análisis de impacto de las novedades que lo requieran.
