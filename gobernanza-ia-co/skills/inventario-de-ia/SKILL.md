---
name: inventario-de-ia
description: >
  Levanta y mantiene el inventario de sistemas de inteligencia artificial con propósito,
  datos, proveedor, decisiones que afecta y responsable. Actívela ante «inventario de
  IA», «qué sistemas de IA tenemos», «registro de algoritmos», «shadow AI», «nadie sabe
  qué herramientas usan las áreas», «gobernanza de IA», o antes de cualquier política de
  uso de IA.
---

# Inventario de IA

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/gobernanza-ia-co/CLAUDE.md`.

> **No se puede gobernar lo que no se conoce.** El inventario es el primer entregable de
> cualquier programa de gobernanza de IA, y el que revela el problema real: casi siempre
> hay más sistemas de los que la organización cree, y los que más riesgo tienen no fueron
> comprados por TI.

## Paso 1 — Qué cuenta como sistema de IA

Definición operativa amplia, para no dejar cosas por fuera: **todo sistema que produce
salidas —predicciones, recomendaciones, clasificaciones, contenido o decisiones— a partir
de datos, mediante técnicas de aprendizaje automático, estadística avanzada o reglas
complejas, y cuya salida influye en una decisión que afecta a personas o al negocio.**

**Incluir siempre:**

| Categoría | Ejemplos |
|---|---|
| **IA generativa** | Asistentes de texto, código, imagen; chatbots; copilotos |
| **Modelos predictivos** | Scoring crediticio, predicción de rotación, detección de fraude |
| **Clasificación** | Filtros de contenido, categorización de PQR, priorización de casos |
| **Visión** | Reconocimiento facial, lectura de documentos, control de acceso |
| **Voz** | Transcripción, análisis de llamadas, autenticación por voz |
| **Recomendación** | Motores de producto, de contenido, de precios |
| **Automatización con reglas complejas** | Sistemas de decisión automatizada, aunque no usen aprendizaje |
| **IA embebida en software de terceros** | La funcionalidad de IA del CRM, del ERP, del gestor documental |

**Y sobre todo: la *shadow AI*.** Herramientas que las áreas contrataron o usan sin pasar
por TI ni por jurídica: suscripciones individuales, extensiones de navegador,
funcionalidades gratuitas. **Es donde está el riesgo de fuga de datos de clientes.**

**Cómo se encuentra la *shadow AI*:** revisión de gastos con tarjeta corporativa y de
suscripciones; encuesta por áreas sin tono sancionatorio; revisión de accesos y dominios
en la red; preguntar en las reuniones de equipo qué herramientas usan para trabajar.

**El tono importa:** si el levantamiento se percibe como una cacería, la gente no reporta
y el inventario queda incompleto. Presentarlo como habilitación —«queremos poder
autorizar lo que ya funciona»— produce mejores resultados.

## Paso 2 — Los campos del inventario

| Campo | Contenido |
|---|---|
| **ID** | |
| **Nombre y proveedor** | |
| **Área usuaria y responsable con nombre** | |
| **Propósito** | Para qué se usa, en una frase |
| **Estado** | Piloto, producción, descontinuado |
| **Tipo de sistema** | Generativa, predictivo, clasificación, visión, voz, recomendación |
| **Desarrollo** | Propio, de proveedor, de proveedor personalizado, de código abierto |
| **Datos de entrada** | Categorías, origen, volumen |
| **¿Datos personales?** | Cuáles |
| **🔴 ¿Datos sensibles o de menores?** | Salud, biométricos, origen étnico, orientación, menores |
| **¿Datos de clientes bajo reserva?** | Especialmente en firmas de abogados |
| **Salida** | Qué produce |
| **🔴 Qué decisión afecta** | Y si hay revisión humana efectiva |
| **¿Afecta derechos de personas?** | Acceso a crédito, empleo, salud, educación, servicios |
| **¿Los datos salen del país?** | A dónde |
| **¿El proveedor usa los datos para entrenar?** | |
| **Contrato y fecha** | |
| **Evaluación de impacto** | ¿Se hizo? Fecha |
| **Clasificación de riesgo** | Ver `/gobernanza-ia-co:triage-de-caso-de-uso` |
| **Última revisión** | |

**Los dos campos marcados 🔴 son los que definen todo lo demás:** si hay datos sensibles o
si la salida afecta decisiones sobre personas, el sistema entra en la categoría de riesgo
alto y activa controles reforzados.

## Paso 3 — El marco colombiano que aplica

No hay todavía una ley general de IA en Colombia. **El marco existente sí aplica**, y es
más exigente de lo que la mayoría supone:

| Marco | Qué exige |
|---|---|
| **Ley 1581 de 2012** | Finalidad determinada, autorización, calidad del dato, seguridad, derechos del titular. **Entrenar un modelo con datos recogidos para otra finalidad viola el principio de finalidad** |
| **Constitución, arts. 13, 15 y 29** | Igualdad y no discriminación, habeas data, debido proceso frente a decisiones que afectan derechos |
| **Ley 1266 de 2008** | Dato financiero y crediticio: reglas propias para scoring |
| **Ley 1480 de 2011** | Información al consumidor cuando la IA interviene en la relación de consumo |
| **Ley 1712 de 2014** | Transparencia y acceso a la información pública: aplica a IA en el sector público |
| **Ley 2213 de 2022 y lineamientos del Consejo Superior de la Judicatura** | Uso de IA en actuaciones judiciales `[verificar]` |
| **Ley 1123 de 2007** | Deberes de diligencia y reserva del abogado que usa IA |
| **CONPES de política nacional de IA** | Lineamientos de política pública `[verificar número, fecha y contenido]` |
| **Regulación sectorial** | Superintendencia Financiera, Supersalud y otras pueden tener exigencias propias `[verificar]` |

**Y el marco extranjero, cuando aplica:** si hay titulares o usuarios en la Unión Europea,
el **Reglamento de IA de la UE** y el **GDPR** pueden aplicar extraterritorialmente
`[verificar aplicabilidad al caso]`.

## Paso 4 — El mantenimiento

| Disparador | Acción |
|---|---|
| Nueva herramienta contratada | Alta en el inventario **antes** de la contratación |
| Cambio de uso de una existente | Reevaluación de riesgo |
| Actualización mayor del modelo | Reevaluación |
| Cambio en los términos del proveedor | Revisión contractual |
| Novedad normativa | Ver `/regulatorio-co:analisis-de-impacto` |
| Revisión periódica | Al menos anual; semestral para riesgo alto |

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Inventario de IA — [organización] — [fecha]

### Resumen
| Métrica | Valor |
|---|---|
| Sistemas identificados | |
| En producción / piloto | |
| Con datos personales | |
| **Con datos sensibles o de menores** | |
| **Que afectan decisiones sobre personas** | |
| Con datos que salen del país | |
| Con evaluación de impacto hecha | |
| **Sin responsable asignado** | |
| **Detectados como *shadow AI*** | |

### Inventario
| ID | Sistema | Proveedor | Área | Propósito | Datos | ¿Sensibles? | Decisión que afecta | ¿Revisión humana? | Riesgo | Responsable | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|

### 🔴 Hallazgos que exigen acción
| Hallazgo | Sistema | Riesgo | Acción | Responsable | Plazo |
|---|---|---|---|---|---|
[p. ej.: datos de clientes bajo reserva profesional cargados en una herramienta gratuita
sin contrato]

### Shadow AI
| Herramienta | Área | Cómo se detectó | Datos que procesa | Decisión |
|---|---|---|---|---|

### Cobertura del levantamiento
**Áreas encuestadas:** [ ] — **Áreas pendientes:** [ ]
**Métodos usados:** [encuesta / revisión de gastos / revisión de red / entrevistas]
**Limitaciones:** [decir explícitamente qué no se revisó]

### Siguiente paso
[Triage de los sistemas de riesgo alto → `/gobernanza-ia-co:triage-de-caso-de-uso`]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Buscar activamente la *shadow AI*.** Un inventario que solo incluye lo que compró TI
  está incompleto por diseño.
- **Todo sistema sin responsable asignado va en sección propia.**
- **Datos sensibles o de clientes bajo reserva en herramientas sin contrato es 🔴
  inmediato**, y va antes del resto del inventario.
- **Declarar la cobertura y las limitaciones del levantamiento.**
- **No calificar un sistema como de bajo riesgo sin mirar qué decisión afecta.**

## Lo que esta skill NO hace

- No audita técnicamente los sistemas.
- No evalúa desempeño ni sesgo de modelos.
- No decide qué se prohíbe: eso es `/gobernanza-ia-co:politica-de-uso-de-ia`.
