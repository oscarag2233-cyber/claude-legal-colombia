---
name: analisis-de-responsabilidad
description: >
  Determina el régimen de responsabilidad civil aplicable —contractual o
  extracontractual, por el hecho propio, por el hecho ajeno, por las cosas o por
  actividades peligrosas—, mapea sus elementos contra la prueba disponible y evalúa las
  causales de exoneración. Actívela ante «¿quién responde?», «responsabilidad civil»,
  «me causaron un daño», «un accidente», «negligencia», «culpa», «responsabilidad
  médica», «responsabilidad del transportador», o cuando alguien pregunte si puede
  reclamar por un daño.
---

# Análisis de responsabilidad

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/responsabilidad-civil-co/CLAUDE.md`.
Si hay datos de salud o de menores, aplicar `referencias/tratamiento-de-datos.md`.

## Paso 1 — ¿Contractual o extracontractual?

Esta decisión cambia todo: el régimen probatorio, la prescripción, la previsibilidad del
daño y hasta el juez.

| Punto | Contractual | Extracontractual |
|---|---|---|
| Fuente | Incumplimiento de obligación preexistente | Deber genérico de no dañar |
| Norma base | CC arts. 1602, 1604, 1613-1616 | CC arts. 2341 y ss. |
| Perjuicios | Solo los **previsibles** si hay buena fe (art. 1616); todos si hay dolo | Todos los ciertos y directos |
| Graduación de culpa | Sí (art. 1604: culpa grave, leve, levísima, según a quién beneficie el contrato) | No hay graduación |
| Prescripción | 10 años (acción ordinaria) | 10 años `[verificar la posición vigente]` |
| Solidaridad | Solo si se pacta o la ley la establece | Sí entre coautores (CC art. 2344) |

**No se puede optar libremente entre los dos regímenes** (regla de no acumulación u
opción restringida). Si hay contrato y el daño deriva de su incumplimiento, la vía es
contractual. Las excepciones —daño a la persona, dolo, obligaciones de seguridad— son
discutidas: `[verificar la línea vigente de la Sala Civil]`.

## Paso 2 — El régimen específico

### Responsabilidad por el hecho propio (CC art. 2341)

Régimen **subjetivo**: hay que probar culpa o dolo, daño y nexo causal. La carga es del
demandante.

### Responsabilidad por el hecho ajeno (CC arts. 2346-2349)

| Responsable | Por quién | Régimen |
|---|---|---|
| Padres | Hijos menores que habiten con ellos | Culpa presunta, desvirtuable |
| Tutores y curadores | Pupilos | Culpa presunta |
| Directores de colegios | Discípulos mientras están a su cuidado | Culpa presunta |
| **Empresarios / patronos (art. 2349)** | Daños causados por sus criados o sirvientes **con ocasión del servicio** | Se exonera probando que no pudo impedir el hecho con la autoridad y cuidado ordinarios |

La responsabilidad del empresario por hechos de sus dependientes es de las más usadas en
la práctica. Verificar: vínculo de dependencia, y que el daño se haya causado **en
ejercicio o con ocasión de las funciones**.

### Responsabilidad por actividades peligrosas (CC art. 2356)

**Este es el régimen más importante de la práctica colombiana.** La jurisprudencia
construyó sobre el art. 2356 un régimen de **culpa presunta** —o, según la formulación
que se prefiera, de responsabilidad objetivada— para quien ejerce actividades que
generan peligro: conducción de vehículos, manejo de energía eléctrica, armas de fuego,
sustancias peligrosas, construcción, actividades industriales.

Consecuencias prácticas:

- **El demandante prueba: la actividad peligrosa, el daño y el nexo causal.** No prueba
  la culpa.
- **El demandado solo se exonera probando causa extraña**: fuerza mayor o caso fortuito,
  **culpa exclusiva de la víctima** o **hecho exclusivo de un tercero**. La diligencia no
  lo exonera.
- **Guardián de la actividad:** responde quien tiene el poder de dirección, control y
  aprovechamiento. El propietario del vehículo suele responder junto con el conductor.
- **Colisión de actividades peligrosas** (dos vehículos): la jurisprudencia ha oscilado
  entre neutralizar las presunciones y mantenerlas. `[verificar la línea vigente de la
  Sala Civil]`

### Responsabilidad por las cosas (CC arts. 2350-2355)

Ruina de edificio, cosa que cae de la parte superior de un edificio, animales
(arts. 2353-2354, con régimen más severo para el animal fiero).

### Regímenes especiales que hay que tener presentes

| Materia | Régimen |
|---|---|
| **Transporte** | C.Co. arts. 981 y ss.: el transportador responde de la conducción de personas y cosas; **obligación de resultado** en el transporte de personas, con presunción de culpa (art. 1003 y 982) `[verificar]` |
| **Producto defectuoso** | Ley 1480 de 2011, arts. 20-22: responsabilidad **objetiva y solidaria** de productor y expendedor por daño causado por producto defectuoso |
| **Médica** | Régimen contractual en general; obligación de **medio** salvo excepciones (cirugía estética, laboratorio). Carga de la prueba y carga dinámica (CGP art. 167) |
| **Del Estado** | Const. art. 90 — daño antijurídico imputable. Va por `/contencioso-administrativo-co:reparacion-directa` |
| **Tránsito** | CC art. 2356 + Ley 769 de 2002 + SOAT. Ver `/responsabilidad-civil-co:reclamacion-a-aseguradora` |

## Paso 3 — Los elementos, contra la prueba

| Elemento | Qué hay que probar | Prueba disponible | Suficiencia |
|---|---|---|---|
| **Hecho** | La conducta o la actividad | | |
| **Daño** | Cierto, personal y no reparado. Puede ser futuro si es cierto | | |
| **Nexo causal** | Que el daño es consecuencia del hecho | | |
| **Culpa** | Solo en régimen subjetivo | | |
| **Imputación** | Quién responde y por qué título | | |

**El nexo causal es donde se pierden los casos.** No basta la secuencia temporal. En
responsabilidad médica, en particular, hay que mostrar que la conducta debida habría
evitado el daño con probabilidad suficiente.

## Paso 4 — Exoneración

| Causal | Requisitos | Efecto |
|---|---|---|
| **Fuerza mayor o caso fortuito** | Imprevisible **e** irresistible, y exterior a la actividad (CC art. 64, mod. Ley 95 de 1890) | Exonera totalmente |
| **Culpa exclusiva de la víctima** | Que la conducta de la víctima sea la causa única | Exonera totalmente |
| **Hecho exclusivo de un tercero** | Que sea causa única y no imputable al demandado | Exonera totalmente |
| **Concurrencia de culpas** (CC art. 2357) | La víctima se expuso imprudentemente | **Reduce** la indemnización, no exonera |
| **Consentimiento de la víctima** | Limitado; no vale para daños a la vida o integridad | |

**La diligencia no exonera en actividades peligrosas.** Es el error más frecuente de la
defensa.

## Paso 5 — Legitimación y solidaridad

- **Por activa:** la víctima directa, y las **víctimas indirectas** o por rebote
  (familiares que sufren perjuicio moral propio). Verificar parentesco con registros
  civiles.
- **Por pasiva:** autor, guardián de la actividad, propietario, empleador (art. 2349),
  asegurador (acción directa del C.Co. art. 1133).
- **Solidaridad** (CC art. 2344): si el daño lo causan varios, responden solidariamente.
  El que paga puede repetir.
- **Llamamiento en garantía** al asegurador (CGP art. 64).

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Análisis de responsabilidad — [asunto]

### Régimen aplicable
**Contractual / extracontractual:** [ ] — por [razón]
**Régimen específico:** [hecho propio / hecho ajeno / actividades peligrosas / especial]
**Consecuencia probatoria:** [qué le toca probar a cada quien]

### Elementos
[la tabla de elementos, con la prueba y su suficiencia]

### Legitimación
| Por activa | Vínculo | Prueba |
|---|---|---|
| Por pasiva | Título de imputación | Solvencia |

### Exoneraciones previsibles de la contraparte
| Causal | Fuerza | Cómo se contrarresta |
|---|---|---|

### Concurrencia de culpas
[¿hay exposición imprudente de la víctima? — porcentaje estimado de reducción]

### 🔴 Prescripción
[término, norma, vencimiento, margen]

### Conclusión
[Hay caso / no hay caso / falta prueba de X]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No afirmar que un régimen es «objetivo» sin decir en qué se funda.** La formulación
  varía y la contraparte va a discutirla.
- **El nexo causal débil es 🔴**, no un detalle.
- **Si la prescripción está próxima, va primero.**
- **En responsabilidad médica**, no emitir juicio sobre la conducta médica sin concepto
  técnico: marcar la necesidad de dictamen.

## Lo que esta skill NO hace

- No liquida — para eso está `/responsabilidad-civil-co:liquidar-perjuicios`.
- No emite conceptos técnicos ni médicos.
- No decide demandar — para eso está `/responsabilidad-civil-co:viabilidad-de-litigio`.
