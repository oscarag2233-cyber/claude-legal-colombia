---
name: evaluacion-de-impacto-ia
description: >
  Evaluación de impacto que cruza el régimen colombiano de datos personales con los
  derechos fundamentales que un sistema de IA puede afectar, con medidas de mitigación y
  decisión documentada. Actívela ante «evaluación de impacto de IA», «análisis de riesgo
  algorítmico», «este modelo puede discriminar», «impacto en derechos», «EIPD para un
  sistema de IA», o cuando el triage haya clasificado un caso como de riesgo alto.
---

# Evaluación de impacto de IA

**Antes de empezar.** Correr `/gobernanza-ia-co:triage-de-caso-de-uso`. Esta evaluación es
para los casos 🟠 de riesgo alto; para los 🟡 basta la versión simplificada.

> **En Colombia no existe todavía un mandato legal general de evaluación de impacto
> algorítmico.** Se hace porque: (i) el principio de responsabilidad demostrada
> —*accountability*— de la Ley 1581 lo respalda; (ii) es la única forma de acreditar
> diligencia si el sistema causa un daño; y (iii) cuando la regulación llegue, el sistema
> ya estará documentado. `[verificar si hay mandato sectorial aplicable]`

## Sección 1 — Descripción del sistema

| Campo | Contenido |
|---|---|
| Nombre, proveedor y versión | |
| Propósito declarado | |
| **Propósito real** | A veces difiere: preguntar cómo se usa, no cómo se diseñó |
| Población afectada y su tamaño | |
| Datos de entrada y su origen | |
| Datos de entrenamiento y su procedencia | |
| Salida | |
| **Decisión que se toma con esa salida** | |
| Grado de automatización | Sugerencia / decisión con revisión / decisión automática |
| Frecuencia de uso | |
| Alternativa actual | Qué se hace hoy sin el sistema |

**El campo «alternativa actual» es el más útil y el que casi nunca se llena.** La pregunta
correcta no es «¿es riesgoso el sistema?», sino «¿es más riesgoso que el proceso humano
que reemplaza?». Un proceso humano con sesgos no documentados puede ser peor que un modelo
medido.

## Sección 2 — Necesidad y proporcionalidad

1. **¿Qué problema resuelve?** En términos verificables.
2. **¿Hay una alternativa menos intrusiva** que logre un resultado equivalente?
3. **¿El beneficio esperado justifica el tratamiento de datos y el riesgo?**
4. **¿Se están usando más datos de los necesarios?** Principio de minimización.

**Si la respuesta a 2 es sí, el análisis se detiene ahí:** existe la obligación de escoger
la alternativa menos intrusiva. Decirlo antes de invertir en mitigaciones de un sistema
que no debió escogerse.

## Sección 3 — Tratamiento de datos personales

Ver `/datos-personales-co:evaluacion-de-tratamiento`. Puntos críticos en IA:

| Punto | Pregunta |
|---|---|
| **Finalidad** | ¿Los datos se recogieron para esta finalidad? **Usar datos de clientes recogidos para prestar un servicio, para entrenar un modelo, es un cambio de finalidad** que requiere nueva base |
| **Autorización** | ¿Cubre el entrenamiento? ¿El perfilamiento? ¿La toma de decisiones automatizada? |
| **Datos sensibles** | ¿Se tratan? ¿Con qué excepción del art. 6? ¿Se pueden inferir aunque no se recojan? |
| **Inferencia de datos sensibles** | Un modelo puede inferir salud, orientación o etnia a partir de datos aparentemente neutros. **El dato inferido es un dato personal** |
| **Calidad del dato** | Datos incompletos, desactualizados o erróneos producen decisiones erróneas y vulneran el principio de veracidad |
| **Conservación** | ¿Cuánto se guardan los datos de entrada y las salidas? |
| **Transferencias** | → `/datos-personales-co:transferencia-internacional` |
| **Derechos del titular** | ¿Puede conocer, actualizar, rectificar y suprimir? ¿Cómo se ejecuta una supresión en un modelo ya entrenado? |
| **Seguridad** | Acceso, cifrado, registro de auditoría |

**La pregunta de la supresión no tiene respuesta fácil y hay que abordarla:** si un titular
pide la supresión de sus datos y el modelo ya se entrenó con ellos, ¿qué se hace?
Documentar la respuesta —reentrenamiento programado, exclusión de datos futuros,
imposibilidad técnica justificada— es parte de la evaluación.

## Sección 4 — Derechos fundamentales

| Derecho | Riesgo típico | Cómo se evalúa |
|---|---|---|
| **Igualdad y no discriminación** (Const. art. 13) | Resultados diferenciados por sexo, raza, edad, discapacidad, origen, religión, opinión | Medir tasas de resultado por grupo; buscar variables *proxy* (barrio, colegio, nombre) |
| **Habeas data** (art. 15) | Tratamiento sin base, perfilamiento no informado | Sección 3 |
| **Debido proceso** (art. 29) | Decisión sin motivación, sin posibilidad de controvertir | ¿Hay explicación? ¿Hay recurso? ¿Hay revisión humana? |
| **Intimidad** (art. 15) | Inferencias sobre la vida privada | |
| **Libertad de expresión** (art. 20) | Moderación automatizada de contenido | |
| **Trabajo** (art. 25) | Vigilancia, evaluación automatizada, decisiones de desvinculación | |
| **Acceso a servicios esenciales** | Exclusión algorítmica de salud, crédito, educación | |
| **Derechos de niños** (art. 44) | Interés superior; tratamiento de sus datos | |

### El análisis de resultados diferenciados

No basta con no usar variables protegidas. Hay que medir:

1. **Definir los grupos** relevantes según el contexto.
2. **Medir la tasa de resultado favorable por grupo.**
3. **Comparar.** Una diferencia sustancial exige explicación.
4. **Buscar *proxies*:** variables neutras que correlacionan con características
   protegidas —lugar de residencia, colegio, tipo de teléfono, hora de conexión—.
5. **Documentar la explicación** de las diferencias que se mantengan, o corregirlas.

**Si no se puede medir, decirlo.** Un sistema cuyo desempeño por grupo no se puede medir es
un sistema cuyo riesgo de discriminación no se puede descartar, y eso es un hallazgo, no
un vacío.

## Sección 5 — Explicabilidad y trazabilidad

| Pregunta | Por qué |
|---|---|
| ¿Se puede explicar **por qué** el sistema produjo una salida concreta? | Debido proceso; atención de reclamos |
| ¿Se puede reconstruir una decisión pasada? | Trazabilidad: qué versión del modelo, con qué datos, qué salida, quién revisó |
| ¿Se conservan los registros? | Por cuánto tiempo |
| ¿La explicación es comprensible para la persona afectada? | Una explicación técnica que nadie entiende no cumple el fin |

## Sección 6 — Mitigaciones y decisión

| Mitigación | Cuándo |
|---|---|
| Reducir el alcance del sistema | |
| Excluir variables o *proxies* | |
| Elevar el umbral de intervención humana | |
| **Revisión humana efectiva** con criterios escritos | Siempre en riesgo alto |
| Mecanismo de reclamación y de revisión de la decisión | |
| Información previa a las personas afectadas | |
| Monitoreo con métricas y umbrales de alerta | |
| Auditoría periódica | |
| Plan de apagado | Qué se hace si el sistema falla |
| Cláusulas contractuales con el proveedor | → `/gobernanza-ia-co:revision-de-proveedor-ia` |

**La decisión se documenta con su fecha, su responsable y su fundamento**, incluso cuando
es favorable. Es lo que acredita diligencia si algo sale mal.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Evaluación de impacto — [sistema]

### Decisión
**[PUEDE OPERAR / PUEDE OPERAR CON MITIGACIONES / NO PUEDE OPERAR COMO ESTÁ]**
**Riesgo residual:** [🔴/🟠/🟡/🟢] — **Revisión:** [fecha]

### 1. El sistema
### 2. Necesidad y proporcionalidad
| Pregunta | Respuesta |
|---|---|
| Problema que resuelve | |
| **¿Hay alternativa menos intrusiva?** | |
| Beneficio esperado vs. riesgo | |
| Minimización de datos | |

### 3. Datos personales
| Punto | Estado | Brecha |
|---|---|---|

### 4. Derechos fundamentales
| Derecho | Riesgo | Probabilidad | Impacto | Nivel |
|---|---|---|---|---|

### Resultados diferenciados
| Grupo | Tasa de resultado favorable | Diferencia | Explicación | ¿Justificada? |
|---|---|---|---|---|
[o: **NO SE PUDO MEDIR — [razón] — esto es un hallazgo 🔴**]

### 5. Explicabilidad y trazabilidad
| Punto | Estado |
|---|---|

### 6. Mitigaciones
| Riesgo | Mitigación | Responsable | Plazo | Riesgo residual |
|---|---|---|---|---|

### Monitoreo
| Métrica | Umbral de alerta | Frecuencia | Responsable |
|---|---|---|---|

### Decisión documentada
**Aprobó:** [nombre y cargo] — **Fecha:** [ ] — **Fundamento:** [ ]
**Próxima revisión:** [fecha] — **Disparadores de revisión anticipada:** [ ]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Si existe una alternativa menos intrusiva, decirlo y detener el análisis ahí.**
- **Si no se puede medir el desempeño por grupo, eso es un hallazgo 🔴**, no un dato
  faltante.
- **Entrenar con datos recogidos para otra finalidad requiere nueva base de
  legitimación.** No pasarlo por alto.
- **Abordar expresamente la supresión de datos en modelos ya entrenados.**
- **Documentar la decisión incluso cuando es favorable.**

## Lo que esta skill NO hace

- No audita técnicamente el modelo ni corre las pruebas: define qué hay que medir.
- No sustituye el criterio del comité que aprueba.
- No certifica cumplimiento.
