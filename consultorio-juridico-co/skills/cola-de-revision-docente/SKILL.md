---
name: cola-de-revision-docente
description: >
  Organiza la cola de revisión del docente con lo que necesita para revisar rápido y bien,
  y asegura que ninguna pieza salga del consultorio sin aval. Actívela ante «cola de
  revisión», «el docente tiene que revisar esto», «qué le mando al profesor», «revisión
  docente», «ficha de revisión», «tengo diez memoriales por revisar».
---

# Cola de revisión docente

> **Ninguna pieza sale del consultorio sin revisión y aval del docente.** No es un trámite:
> es el fundamento de que un estudiante pueda actuar. La responsabilidad profesional es
> del abogado que supervisa (Decreto 196 de 1971; Ley 1123 de 2007).

**Antes de empezar.** Leer el perfil: docentes por área y protocolo de revisión.

## El problema que resuelve

Un docente de consultorio revisa decenas de piezas por semana, en tiempo que casi siempre
es insuficiente. **Si cada pieza llega sin contexto, la revisión se vuelve superficial** —o
el docente termina reconstruyendo el caso desde cero—.

La solución es que **cada pieza llegue con lo que el docente necesita para decidir en
minutos**: qué se hizo, en qué se duda, qué hay que verificar, y cuándo vence.

## La ficha de revisión

Toda pieza sube a la cola con esta carátula. Sin carátula, no entra a la cola.

```markdown
## Ficha de revisión — Caso [n.º] — [pieza]

**Estudiante:** [ ] · **Docente:** [ ] · **Área:** [ ]
**🔴 Vence:** [fecha] · **Días hábiles restantes:** [N]
**Tiempo estimado de revisión:** [ ]

### En una frase
[Qué es este caso y qué se pretende con esta pieza]

### Lo que ya está resuelto
[Lo que el estudiante verificó y no necesita revisión: competencia, término, requisitos]

### 🔴 Dudas concretas para el docente
1. [Duda específica, no «revíseme el escrito»]
2. [ ]

### Decisiones que tomé y que pueden discutirse
| Decisión | Por qué la tomé | Alternativa que descarté |
|---|---|---|

### Verificación de citas
| Cita | Fuente consultada | ¿Verificada? |
|---|---|---|
[Ver `/consultorio-juridico-co:verificar-citas`]

### Anexos
[Ficha de consulta, documentos, pieza]
```

**La sección de dudas concretas es la que hace útil la ficha.** «Revíseme el escrito» le
traslada todo el trabajo al docente. «No estoy seguro de si la causal es la del numeral 2
o la del 8, porque los hechos permiten las dos lecturas» le permite responder en dos
minutos.

## La cola

| Campo | Contenido |
|---|---|
| Prioridad | Por vencimiento, no por orden de llegada |
| Caso y pieza | |
| Estudiante y docente | |
| Fecha de entrada a la cola | |
| **Días en cola** | |
| Vencimiento del término | |
| Estado | En cola / en revisión / devuelta con observaciones / avalada / radicada |
| N.º de devoluciones | |

**Regla de la cola:** se ordena por **vencimiento**, no por antigüedad. Una pieza que
entró hoy y vence pasado mañana va antes que una que entró la semana pasada y vence en un
mes.

**Alerta de estancamiento:** una pieza con más de 3 días hábiles en cola y con término
próximo se escala al director del consultorio.

## Lo que revisa el docente

Lista sugerida, para que la revisión sea consistente entre docentes:

| # | Verificación | Consecuencia si falla |
|---|---|---|
| 1 | **Competencia del consultorio** para el asunto | No se puede actuar |
| 2 | **Término**: cálculo, norma, calendario judicial | Se pierde el caso |
| 3 | **Requisitos de procedibilidad** | Inadmisión |
| 4 | **Legitimación** de las partes | Excepción |
| 5 | **Poder** y su alcance | Falta de representación |
| 6 | **Requisitos formales** de la pieza | Inadmisión |
| 7 | **Hechos**: completos, numerados, con fecha, con prueba | Se cae en el proceso |
| 8 | **Pretensiones**: claras, consecuenciales, completas | Fallo incongruente |
| 9 | **Fundamento de derecho**: norma vigente, aplicable | |
| 10 | **🔴 Citas verificadas** | Riesgo disciplinario |
| 11 | **Pruebas**: pedidas correctamente, con objeto | Rechazo de prueba |
| 12 | **Anexos** completos | Inadmisión |
| 13 | **Notificaciones**: dirección física y electrónica | Estancamiento |
| 14 | **Redacción y respeto al despacho** | |
| 15 | **Coherencia con lo que se le dijo al usuario** | |

## Las devoluciones que enseñan

Una devolución que dice «corregir» no enseña. La que enseña dice **qué está mal, por qué,
y qué se espera**:

| ❌ | ✅ |
|---|---|
| «Revisar los hechos» | «Los hechos 4 y 7 no tienen fecha. Sin fecha no se puede acreditar la oportunidad de la reclamación. Agregue la fecha o explique por qué no se conoce» |
| «Falta fundamentación» | «El escrito invoca el art. 62 del CST pero no dice cuál literal ni cuál numeral. Precíselo: la causal determina qué hay que probar» |
| «Mal calculado» | «El término se contó desde la fecha de la carta y debe contarse desde la notificación, que fue el [fecha]. Recalcule y verifique contra el calendario judicial» |

**Cada devolución es una clase.** Es el momento de mayor rendimiento pedagógico del
consultorio, y se desperdicia con observaciones genéricas.

## El aval

Cuando el docente avala, queda constancia:

```
AVALADO POR: [Nombre del docente], abogado, T.P. n.º [ ]
FECHA: [ ]
OBSERVACIONES: [las que queden]
AUTORIZA RADICAR: SÍ
```

**El aval es lo que permite que la pieza salga.** Sin él, la pieza no se radica, no se
entrega al usuario y no se envía a ninguna autoridad.

## Salida

```markdown
[NOTAS DE TRABAJO — CONSULTORIO JURÍDICO]

## Cola de revisión — [fecha]

### 🔴 Revisar hoy
| Caso | Pieza | Vence | Días en cola | Estudiante | Docente | Duda principal |
|---|---|---|---|---|---|---|

### 🟠 Esta semana
### 🟡 Programadas

### ⚠️ Estancadas (más de 3 días en cola con término próximo)
| Caso | Pieza | Días en cola | Vence | Docente | **Escalar a dirección** |
|---|---|---|---|---|---|

### Devueltas pendientes de corrección
| Caso | Devuelta el | Observaciones | Vence | Estudiante |
|---|---|---|---|---|

### Avaladas pendientes de radicar
| Caso | Pieza | Avalada el | Vence | Responsable de radicar |
|---|---|---|---|---|
[Una pieza avalada y no radicada es un término perdido con aval]

### Métricas de la semana
| Métrica | Valor |
|---|---|
| Piezas revisadas | |
| Devueltas | |
| Tiempo promedio en cola | |
| Motivos de devolución más frecuentes | **[esto indica qué hay que reforzar en clase]** |
```

## Compuertas

- **Ninguna pieza sin ficha de revisión entra a la cola.**
- **Ninguna pieza sale sin aval expreso del docente.**
- **La cola se ordena por vencimiento.**
- **Las piezas avaladas y no radicadas se reportan:** el aval no radica solo.
- **Las devoluciones se escriben con el qué, el porqué y lo que se espera.**

## Lo que esta skill NO hace

- No revisa por el docente: organiza para que revise bien.
- No avala.
- No radica.
