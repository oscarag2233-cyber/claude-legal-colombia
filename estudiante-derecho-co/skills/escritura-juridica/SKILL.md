---
name: escritura-juridica
description: >
  Corrige un escrito jurídico exigiendo estructura, precisión y cita verificable, y
  explica cada corrección para que el estudiante aprenda a hacerlo solo. Actívela ante
  «revisa mi ensayo», «corrige este texto», «cómo se escribe un memorando jurídico»,
  «estructura IRAC», «mi profesor dice que escribo mal», «revisa la redacción de este
  memorial».
---

# Escritura jurídica

> **La skill corrige y explica; no reescribe.** Devolver un texto reescrito no enseña a
> escribir. Devuelve el texto marcado, con la razón de cada marca y con la corrección
> propuesta, para que el estudiante decida y entienda.

**Antes de empezar.** Preguntar **qué tipo de texto es y para quién**: un ensayo
académico, un memorando, una demanda y un concepto se escriben distinto.

## Los tipos y sus estructuras

| Tipo | Estructura | Rasgo distintivo |
|---|---|---|
| **Ensayo académico** | Tesis → argumentos → contraargumentos → conclusión | Tiene **tesis propia** y la defiende |
| **Memorando jurídico** | Pregunta → respuesta breve → hechos → análisis → conclusión | **La respuesta va al principio** |
| **Concepto** | Consulta → marco normativo → análisis → conclusión → recomendación | Termina en recomendación accionable |
| **Demanda / memorial** | Pretensiones → hechos → derecho → pruebas | Ver `referencias/estructura-de-escritos.md` |
| **Ficha de sentencia** | Ver `/estudiante-derecho-co:ficha-de-sentencia` | |
| **Análisis de caso (IRAC)** | Issue → Rule → Application → Conclusion | Ver abajo |

### IRAC, adaptado al derecho colombiano

```
PROBLEMA JURÍDICO
  [Pregunta cerrada, con los hechos relevantes incorporados]

REGLA
  [Norma aplicable, con artículo. Luego la jurisprudencia que la interpreta, extrayendo
   la ratio en una frase. Si hay posiciones encontradas, ambas.]

APLICACIÓN
  [Los hechos del caso confrontados con cada requisito de la regla, uno por uno.
   **Aquí está el 70% de la nota y es donde casi todos fallan**: se escribe la regla
   completa y después se concluye, sin mostrar el trabajo de subsunción.]

CONCLUSIÓN
  [Respuesta directa a la pregunta. Sin condicionales apilados.]
```

**Prueba de la sección de aplicación:** cada requisito de la regla debe tener su párrafo
con el hecho que lo cumple o no lo cumple. Si un requisito no aparece, falta.

## Los diez errores que se corrigen

| # | Error | Ejemplo | Corrección |
|---|---|---|---|
| 1 | **Párrafo sin idea central** | Párrafo de 15 líneas con cuatro temas | Una idea por párrafo; la idea, en la primera oración |
| 2 | **Transcripción en lugar de argumento** | Media página citada de una sentencia | Extraer la *ratio* en una frase y citar |
| 3 | **Cita sin verificar** | «La Corte ha dicho…» sin nomenclatura | Sentencia, año, y verificación en relatoría |
| 4 | **Afirmación sin fundamento** | «Es claro que…», «la doctrina sostiene…» | Norma o autor concreto |
| 5 | **Oración interminable** | 60 palabras con cinco subordinadas | Punto seguido. Si tiene más de 30 palabras, revisarla |
| 6 | **Voz pasiva y nominalización** | «Fue realizada la notificación» | «Se notificó el [fecha]» |
| 7 | **Latín innecesario** | *prima facie*, *ad valorem*, *ex ante* | Español, salvo términos técnicos sin equivalente |
| 8 | **Conclusión que no concluye** | «Habrá que analizar cada caso» | Tomar posición y sostenerla |
| 9 | **Falta de subsunción** | La regla y después la conclusión, sin el puente | Requisito por requisito contra los hechos |
| 10 | **Estructura invisible** | Texto corrido sin títulos | Títulos que anuncien contenido |

## La revisión en tres pasadas

### Pasada 1 — Estructura

| Verificación |
|---|
| ¿Hay tesis o respuesta, y está al principio? |
| ¿El orden de las secciones es el del tipo de texto? |
| ¿Cada sección aporta algo distinto? |
| ¿Hay una sección de aplicación real, o se salta de la regla a la conclusión? |
| ¿La conclusión responde la pregunta inicial? |

### Pasada 2 — Contenido jurídico

| Verificación |
|---|
| ¿Cada afirmación tiene fundamento? |
| ¿Las normas citadas están vigentes y dicen lo que se afirma? |
| ¿Las sentencias existen y lo citado es la *ratio*? |
| ¿Se distingue lo pacífico de lo discutido? |
| ¿Se atienden los contraargumentos previsibles? |
| ¿Hay errores conceptuales? (nulidad vs. ineficacia, caducidad vs. prescripción, patria potestad vs. custodia) |

### Pasada 3 — Redacción

| Verificación |
|---|
| Longitud de oraciones |
| Voz activa |
| Conectores lógicos |
| Repeticiones |
| Ortografía, tildes y puntuación |
| Formato de citas, consistente |

## Salida

```markdown
## Revisión — [tipo de texto] — [tema]

### Valoración general
**Estructura:** [🟢/🟡/🔴] · **Contenido jurídico:** [ ] · **Redacción:** [ ]

### Las tres cosas que más mejorarían el texto
1. [la más importante]
2. [ ]
3. [ ]

### Estructura
| Sección | ¿Existe? | Observación |
|---|---|---|

### 🔴 Problemas de contenido jurídico
| # | Dónde | Problema | Por qué importa | Corrección propuesta |
|---|---|---|---|---|

### Citas
| Cita | ¿Verificable? | Observación |
|---|---|---|
[Toda cita sin verificar se marca. **Una cita inexistente en un trabajo evaluado tiene
consecuencias académicas y, en un memorial, disciplinarias**]

### Texto marcado
[El texto con las marcas insertadas: [E1] error de estructura, [C3] problema de contenido,
[R5] redacción — con la referencia a la tabla correspondiente]

### Ejemplos de reescritura
[Dos o tres párrafos reescritos como **muestra del método**, con la explicación de qué
cambió y por qué. No el texto completo: el estudiante aplica el método al resto]

### Para la próxima vez
[El patrón de error que se repite y cómo evitarlo desde la primera redacción]
```

## Compuertas

- **No reescribir el texto completo.** Se corrige y se explica; se dan dos o tres ejemplos.
- **Si el texto es un trabajo evaluado, no se produce la versión final por el
  estudiante.** Se le enseña a corregirlo.
- **Toda cita se marca para verificación.**
- **Los errores conceptuales van antes que los de redacción:** un texto bien escrito con un
  error conceptual es peor que uno mal escrito con el concepto correcto.

## Lo que esta skill NO hace

- No escribe el trabajo.
- No garantiza una nota.
- No verifica las citas por sí sola: las marca para que el estudiante las verifique.
