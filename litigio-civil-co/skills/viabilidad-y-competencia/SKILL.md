---
name: viabilidad-y-competencia
description: >
  Filtro previo a redactar cualquier demanda civil o comercial: verifica que la
  pretensión sea viable, que el juez sea competente, que el trámite y la cuantía estén
  bien fijados, que no haya operado caducidad ni prescripción, y que el requisito de
  procedibilidad esté agotado. Actívela ante «¿puedo demandar?», «¿ante quién demando?»,
  «¿cuál es la cuantía?», «¿todavía estoy a tiempo?», «¿tengo que conciliar antes?», o
  cuando el usuario describa un conflicto y pregunte qué hacer.
---

# Viabilidad y competencia

> Esta skill corre **antes** de `/litigio-civil-co:redactar-demanda`. Una demanda bien
> escrita ante juez incompetente, con la cuantía mal fijada o con la acción prescrita,
> es tiempo perdido y a veces es una responsabilidad profesional.

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/litigio-civil-co/CLAUDE.md`.
Si no existe o tiene `[PENDIENTE]` en `## Criterios de la casa`, detenerse y remitir a
`/litigio-civil-co:entrevista-inicial`. Aplican los guardarraíles compartidos del perfil.

*Los artículos que se citan abajo son un mapa, no una fuente. Verifíquelos contra el
texto vigente antes de usarlos en una pieza — el CGP ha sido modificado por la Ley 2213
de 2022 y por reformas posteriores.*

## Los siete filtros, en orden

Se corren en este orden porque cada uno puede matar el caso y ahorra el siguiente.

### 1. ¿Hay derecho? — la pretensión

- ¿Qué se pide exactamente? Traducir el relato del cliente a **pretensiones**:
  declarativas, de condena, constitutivas.
- ¿Cuál es la norma sustancial que soporta cada pretensión?
- ¿La pretensión es de las que un juez puede conceder? (No lo son: obligar a alguien a
  querer, revivir un término vencido, revisar una decisión ejecutoriada por vía
  ordinaria.)
- **Acumulación de pretensiones** (CGP art. 88): mismo juez competente, no excluyentes
  entre sí salvo que se pidan como subsidiarias, y trámite compatible. Una acumulación
  indebida es causal de ineptitud (excepción previa del art. 100 num. 5).

### 2. ¿Todavía se puede? — caducidad y prescripción

Ver `referencias/terminos-caducidad-prescripcion.md`. Fijar:

| Punto | Respuesta |
|---|---|
| ¿Es caducidad o prescripción? | Caducidad se declara de oficio; prescripción hay que alegarla |
| Norma que fija el término | [artículo y ley] |
| Fecha desde la que corre | [hecho + por qué desde ahí] |
| Interrupciones o suspensiones | Reclamo escrito, solicitud de conciliación, demanda anterior |
| Fecha de vencimiento | [fecha] |
| Margen que queda | [días] |

**Si el margen es de menos de 30 días, esto sube a 🔴 y encabeza la salida.** Con
menos de 30 días hay que decidir ya si se concilia primero o si aplica alguna excepción
al requisito de procedibilidad.

### 3. ¿Hay que conciliar antes? — requisito de procedibilidad

La conciliación extrajudicial en derecho es requisito de procedibilidad en asuntos
civiles, comerciales y de familia que sean conciliables (Estatuto de Conciliación,
Ley 2220 de 2022). `[verificar el régimen vigente y sus excepciones]`

Excepciones típicas que hay que revisar caso a caso: procesos ejecutivos, procesos en
que se pidan medidas cautelares, procesos donde se desconozca el domicilio del
demandado, asuntos no conciliables.

**La solicitud de conciliación suspende el término de caducidad o prescripción** hasta
la audiencia o hasta tres meses, lo que ocurra primero. Ese dato salva casos.

### 4. ¿Quién es el juez? — competencia

Cuatro factores, todos:

**Objetiva — por la naturaleza:** civil, comercial, familia, agrario. Ojo con las
**competencias jurisdiccionales de las superintendencias**: la SIC conoce de protección
al consumidor, competencia desleal e infracción de propiedad industrial; la
Superintendencia de Sociedades conoce de conflictos societarios, insolvencia y abuso
del derecho de voto. Si el asunto cabe ahí, decirlo: suele ser más rápido.

**Objetiva — por la cuantía** (CGP arts. 25 y 26):

| Cuantía | Rango | Juez |
|---|---|---|
| Mínima | Hasta 40 SMLMV | Civil municipal — única instancia |
| Menor | Más de 40 y hasta 150 SMLMV | Civil municipal |
| Mayor | Más de 150 SMLMV | Civil del circuito |

La cuantía se fija por el valor de las pretensiones al tiempo de la demanda, sin
intereses ni costas (art. 26). **Con el SMLMV del año de presentación.** Ver
`referencias/valores-anuales.md`.

**Territorial** (CGP art. 28): la regla general es el domicilio del demandado. Fueros
concurrentes usuales: lugar de cumplimiento de la obligación (contractual), lugar donde
ocurrió el hecho (extracontractual), ubicación del inmueble (reales). Cuando hay varios
fueros, elige el demandante.

**Funcional:** primera instancia, segunda instancia, casación.

**Cláusula compromisoria.** Si el contrato tiene pacto arbitral, el juez ordinario no
es competente y el demandado puede proponer la excepción previa del art. 100 num. 2.
Revisarlo **antes** de redactar, no después.

### 5. ¿Por qué trámite? — el proceso

| Trámite | Cuándo | Rasgos |
|---|---|---|
| **Verbal** (arts. 368-373) | Regla general de los declarativos | Traslado de 20 días, audiencia inicial y audiencia de instrucción y juzgamiento |
| **Verbal sumario** (arts. 390-392) | Mínima cuantía y asuntos que la ley señala | Única instancia, traslado de 10 días, audiencia única |
| **Ejecutivo** (arts. 422 y ss.) | Hay título ejecutivo | Ver `/litigio-civil-co:proceso-ejecutivo` |
| **Especiales** | Pertenencia, divisorio, expropiación, deslinde, monitorio (arts. 419-421) | Reglas propias |

El **proceso monitorio** (arts. 419-421) merece mirada aparte: para obligaciones
dinerarias de mínima cuantía sin título ejecutivo, es mucho más rápido. Si el caso cabe
ahí, decirlo.

### 6. ¿Con qué se prueba? — viabilidad probatoria

No es un filtro formal, pero mata más casos que los formales. Para cada hecho
determinante: ¿con qué se prueba, quién lo tiene y se puede conseguir? Si un hecho
central no tiene prueba y no hay cómo conseguirla, decirlo ahora.

### 7. ¿Vale la pena? — el filtro económico

- Cuantía pretendida frente a costo del proceso y honorarios.
- **Solvencia del demandado**: ¿hay bienes? Un fallo contra un insolvente es un papel.
- Duración realista en el circuito donde se va a radicar.
- Escenario de conciliación: ¿qué se conseguiría hoy sin demandar?

Contrastar contra los umbrales de `## Criterios de la casa` del perfil.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según el perfil]

## Viabilidad — [asunto]

**Recomendación:** [DEMANDAR / CONCILIAR PRIMERO / NO DEMANDAR / FALTAN HECHOS]

### Lo que decide

| Filtro | Resultado | Detalle |
|---|---|---|
| Pretensión | ✅ / ⚠️ / 🔴 | [norma sustancial que la soporta] |
| Caducidad / prescripción | ✅ / ⚠️ / 🔴 | Vence [fecha] — quedan [N] días — [norma] |
| Requisito de procedibilidad | ✅ / ⚠️ / 🔴 | [conciliación agotada / pendiente / no aplica porque…] |
| Competencia | ✅ / ⚠️ / 🔴 | [Juez X de Y] — cuantía [mínima/menor/mayor] = [$ y SMLMV del año] |
| Trámite | ✅ | [verbal / verbal sumario / ejecutivo / monitorio] |
| Prueba | ✅ / ⚠️ / 🔴 | [hechos sin respaldo probatorio] |
| Economía del caso | ✅ / ⚠️ / 🔴 | [cuantía vs. costo vs. solvencia] |

### Lo que hay que conseguir antes de radicar
- [documento o dato faltante — quién lo tiene]

### Riesgos
| Riesgo | Severidad | Mitigación |
|---|---|---|

### Alternativas a demandar
[conciliación, requerimiento previo, arbitraje si hay pacto, transacción]

Fuentes: [conectores usados o «sin conector — verificar»] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **🔴 si la caducidad o la prescripción vencen en menos de 30 días.** Va primero en la
  salida, antes que cualquier otra cosa.
- **No decir «demande» si falta el requisito de procedibilidad.** Decir qué hay que
  agotar y cuánto suspende.
- **Si el Rol no es abogado inscrito**, la recomendación de demandar no pasa sin la
  compuerta de revisión profesional del perfil.

## Lo que esta skill NO hace

- No redacta la demanda — para eso está `/litigio-civil-co:redactar-demanda`.
- No garantiza el resultado: evalúa viabilidad, no éxito.
- No consulta el estado de procesos ni verifica bienes del demandado; señala que hay
  que hacerlo.
