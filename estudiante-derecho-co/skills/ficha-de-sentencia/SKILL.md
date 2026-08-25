---
name: ficha-de-sentencia
description: >
  Ficha una sentencia colombiana separando problema jurídico, ratio decidendi, obiter
  dicta, decisum y salvamentos, y la ubica en su línea. Actívela ante «hazme la ficha de
  esta sentencia», «resume esta sentencia», «cuál es la ratio de esta providencia», «qué
  decidió la Corte», «análisis jurisprudencial de una sentencia», «tengo que exponer esta
  sentencia».
---

# Ficha de sentencia

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/estudiante-derecho-co/CLAUDE.md`.

> **Esta skill ficha; no estudia por usted.** El valor de fichar está en la lectura, y por
> eso la skill trabaja **sobre el texto que usted aporte** y le devuelve preguntas además
> de respuestas.

**Si no se aporta el texto de la sentencia, la skill lo pide.** Fichar de memoria produce
exactamente el error que esta skill existe para evitar.

## La anatomía que hay que separar

| Parte | Qué es | Fuerza |
|---|---|---|
| **Decisum** | La orden concreta: resuelve, ordena, declara, confirma, revoca | Obliga a las partes; *erga omnes* en control abstracto |
| **Ratio decidendi** | La regla de derecho **sin la cual la decisión no se sostiene** | **Es lo que constituye precedente** |
| **Obiter dicta** | Consideraciones marginales, ejemplos, derecho comparado, hipótesis | Persuasivo, no vinculante |
| **Salvamentos y aclaraciones de voto** | La posición de los magistrados que se apartan o precisan | No vinculan, pero **anticipan cambios de línea** |

**La prueba de la *ratio*:** si se suprime el enunciado, ¿la decisión sigue en pie?
Si sigue en pie, es *obiter*.

Referentes: Corte Constitucional, SU-047 de 1999 y T-292 de 2006 sobre identificación de
la *ratio*. `[verificar]` Ver `referencias/precedente-y-jurisprudencia.md`.

## Cómo se lee una sentencia colombiana

| Corporación | Estructura típica | Dónde suele estar la *ratio* |
|---|---|---|
| **Corte Constitucional** | Antecedentes → Consideraciones (competencia, problema jurídico, marco, caso concreto) → Decisión | En el desarrollo del problema jurídico y en su aplicación al caso concreto |
| **Corte Suprema — Casación** | Antecedentes → Demanda de casación (cargos) → Consideraciones → Decisión | En la respuesta a cada cargo |
| **Consejo de Estado** | Antecedentes → Consideraciones (competencia, problema, caso) → Decisión | Ídem |

**Truco de lectura:** empezar por el **problema jurídico** que la propia providencia
formula, y por la **parte resolutiva**. Con esos dos extremos, el desarrollo se entiende
mucho más rápido, y se distingue mejor lo necesario de lo accesorio.

## La ficha

```markdown
# [Nomenclatura] — [Corporación, Sala o Sección]

## Identificación
| Campo | Contenido |
|---|---|
| Sentencia | [C-/SU-/T- n.º de año] o [SC/SL/SP n.º-año] |
| Fecha | |
| Corporación y sala | |
| Magistrado ponente | [o «no consta en el texto aportado»] |
| Radicado / expediente | |
| Tipo de proceso | control abstracto / tutela / casación / nulidad / reparación directa |
| Norma o providencia examinada | |

## Hechos relevantes
[Solo los que soportan la decisión. Máximo cinco líneas: si necesita más, probablemente
está incluyendo hechos que no son relevantes.]

## Problema jurídico
[Como lo formula la propia sentencia, entre comillas si es textual. Si la sentencia no lo
formula expresamente, reconstruirlo y decir que es una reconstrucción.]

## Ratio decidendi
> [La regla, en una o dos frases, con la referencia al párrafo o considerando]

**Prueba de necesidad:** [por qué sin este enunciado la decisión no se sostiene]

## Obiter dicta relevantes
- [Enunciado] — *no vinculante, pero útil porque [ ]*

## Decisum
[La parte resolutiva, transcrita o resumida con precisión. En control de
constitucionalidad: **exequible, inexequible, exequible condicionada** — y **el
condicionamiento textual**, que es lo que después hay que aplicar]

## Salvamentos y aclaraciones
| Magistrado | Posición | Argumento central |
|---|---|---|

## Ubicación en la línea
| Punto | Contenido |
|---|---|
| Sentencias que cita como fundamento | |
| ¿Reitera, precisa o cambia la línea? | |
| ¿Es sentencia de unificación o hito? | |
| ¿Hay pronunciamientos posteriores? | `[verificar en la relatoría]` |

## Para qué sirve
| Uso | Cómo se cita |
|---|---|
| [pretensión o defensa que respalda] | [la frase con la que se invocaría] |

## Preguntas para verificar que entendió
1. ¿Cuál era exactamente el problema jurídico?
2. ¿Qué habría pasado si el hecho [X] hubiera sido distinto?
3. ¿La regla aplica a [caso análogo]? ¿Por qué sí o por qué no?
4. ¿Cuál es el enunciado más fuerte del salvamento de voto?
5. ¿Cómo la citaría en un memorial, en una sola frase?

## Verificación
Fuente del texto: [aportado por el usuario / relatoría oficial] `[etiqueta]`
Datos no verificables en el texto aportado: [M.P., radicado, votación]
```

## Errores que esta skill corrige

| Error | Corrección |
|---|---|
| **Citar un *obiter* como si fuera la regla** | La prueba de necesidad lo detecta |
| **Citar una exequibilidad sin su condicionamiento** | El condicionamiento va textual en el decisum |
| **Resumir la sentencia en lugar de extraer la regla** | Un resumen de tres páginas no sirve para nada; una *ratio* de dos frases sí |
| **Confundir la posición del salvamento con la de la Corte** | Van en secciones separadas |
| **Dar por vigente una línea sin verificar posteriores** | Marca `[verificar en la relatoría]` |
| **Inventar el M.P. o el radicado** | Si no consta en el texto, se dice |

## Compuertas

- **No fichar de memoria.** Si no hay texto, se pide.
- **No inventar magistrado ponente, radicado ni votación.**
- **Marcar siempre la necesidad de verificar si la línea sigue vigente.**
- **Devolver las preguntas de comprensión:** son parte del entregable, no un adorno.

## Lo que esta skill NO hace

- No lee la sentencia por el estudiante: la organiza para que la entienda.
- No busca sentencias: ficha las que se le den.
- No garantiza vigencia de la línea.
