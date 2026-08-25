---
name: viabilidad-de-litigio
description: >
  Puntúa un caso de responsabilidad antes de demandar: fuerza probatoria de cada
  elemento, prescripción, solvencia del demandado, costo del proceso, tiempo estimado y
  escenarios de transacción. Actívela ante «¿vale la pena demandar?», «qué
  probabilidades tengo», «cuánto me costaría el proceso», «me conviene transar»,
  «evalúa este caso», o cuando el cliente quiera saber si invertir en un litigio.
---

# Viabilidad de litigio

**Antes de empezar.** Leer el perfil, incluidos los umbrales de `## Criterios de la
casa`. Esta skill produce una **estimación razonada, no un pronóstico**. Decirlo en la
salida.

## Por qué esto se hace antes y no después

El costo de descubrir en la audiencia que no había prueba del nexo causal es el costo de
todo el proceso más el de las costas. Media hora de evaluación honesta al principio le
ahorra al cliente dos años y varios millones.

**Y hay un deber profesional detrás:** informar al cliente con veracidad sobre las
posibilidades de su asunto (Ley 1123 de 2007, art. 33). Prometer resultados o inflar
expectativas es falta disciplinaria.

## Los cinco ejes

### 1. Fuerza jurídica

| Elemento | Peso | Estado probatorio | Puntaje |
|---|---|---|---|
| Hecho / conducta | | ✅ probado / ⚠️ débil / 🔴 sin prueba | |
| Daño | | | |
| Nexo causal | **El que más pesa** | | |
| Culpa (si el régimen la exige) | | | |
| Imputación al demandado | | | |
| Legitimación por activa | | | |

**Regla:** un 🔴 en nexo causal o en legitimación baja el caso a inviable, sin importar
el resto.

**Régimen aplicable:** si es actividad peligrosa, el caso sube: la culpa no hay que
probarla. Ver `/responsabilidad-civil-co:analisis-de-responsabilidad`.

### 2. Riesgo procesal

| Punto | Evaluación |
|---|---|
| **Prescripción / caducidad** | Margen en días. 🔴 si es menos de 60 |
| **Requisito de procedibilidad** | Conciliación agotada o pendiente |
| **Competencia** | Juez, cuantía, trámite |
| **Excepciones previsibles** | Culpa de la víctima, hecho de tercero, fuerza mayor, pago, transacción anterior |
| **Concurrencia de culpas** | Porcentaje estimado de reducción (CC art. 2357) |
| **Calidad de la contraparte** | ¿Litiga bien? ¿Tiene abogado interno? ¿Es aseguradora? |
| **Congestión del despacho** | Tiempo real en el circuito |

### 3. Recuperabilidad — el eje que se olvida

Ganar no es cobrar.

| Punto | Pregunta |
|---|---|
| **Solvencia** | ¿El demandado tiene bienes? ¿Inmuebles, vehículos, cuentas, cuotas sociales? |
| **Aseguradora** | ¿Hay póliza de RC? Si la hay, **el caso cambia de naturaleza**: hay pagador solvente y se puede llamar en garantía o ejercer la acción directa (C.Co. art. 1133) |
| **Riesgo de insolvencia** | ¿Puede vaciar el patrimonio antes de la sentencia? → cautelares |
| **Solidaridad** | ¿Hay otros responsables solventes? (CC art. 2344) |

**Un caso jurídicamente fuerte contra un insolvente sin seguro es un caso débil.**
Decirlo.

### 4. Economía del caso

| Concepto | Estimación |
|---|---|
| Pretensión razonable | $[X] — de `/responsabilidad-civil-co:liquidar-perjuicios` |
| Reducción esperada por el juez | [%] — los jueces suelen conceder menos de lo pedido |
| Reducción por concurrencia de culpas | [%] |
| **Valor esperado bruto** | $[X × probabilidad × (1 − reducciones)] |
| Honorarios | [pactados / de éxito] |
| Costos: peritos, gastos, cauciones | $[ ] |
| **Riesgo de costas** si se pierde | $[ ] |
| Duración estimada | [N] años en primera instancia, [N] con segunda |
| **Valor presente neto** | |

### 5. Escenarios

| Escenario | Probabilidad | Resultado | Cuándo se sabe |
|---|---|---|---|
| Conciliación prejudicial | | $[ ] | En 1-3 meses |
| Allanamiento / transacción temprana | | $[ ] | Año 1 |
| Sentencia favorable primera instancia | | $[ ] | Año [ ] |
| Sentencia favorable en segunda | | $[ ] | Año [ ] |
| Sentencia adversa | | −$[costas] | |

## La conversación de la conciliación

Casi siempre hay una oferta de transacción que le conviene más al cliente que el
proceso, y casi nunca se le presenta con números. Presentarla así:

> Si el caso vale $100 y usted tiene un 60% de probabilidad, con un descuento típico del
> juez del 20% y tres años de espera, el valor presente de litigar está alrededor de
> $[X]. Una transacción hoy por encima de esa cifra le conviene. Por debajo, no.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Viabilidad — [asunto]

### Veredicto
**[VIABLE / VIABLE CON RESERVAS / NO VIABLE / FALTAN ELEMENTOS PARA DECIDIR]**
[Dos líneas de porqué.]

### Fuerza jurídica
[la tabla de elementos]
**Régimen:** [ ] — **Consecuencia probatoria:** [ ]

### Riesgo procesal
[la tabla]
🔴 **Prescripción:** vence [fecha], quedan [N] días

### Recuperabilidad
| Punto | Estado |
|---|---|
| Bienes identificados | |
| Póliza de RC | [SÍ — cambia el caso / NO / se desconoce] |
| Necesidad de cautelares | |

### Economía
[la tabla]

### Escenarios
[la tabla]

### Recomendación
[demandar / conciliar primero / conseguir X antes de decidir / no demandar]

### Lo que cambiaría este análisis
| Si se consigue | El veredicto pasaría a |
|---|---|

---
*Esta es una estimación razonada con la información disponible, no un pronóstico. Los
resultados judiciales dependen de la valoración probatoria del juez y de hechos que aún
no se conocen.*

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No prometer resultados.** El párrafo final de advertencia es obligatorio: prometer
  resultados es falta disciplinaria (Ley 1123 de 2007).
- **Si la prescripción está próxima**, va primero y la recomendación tiene que resolverla
  antes que cualquier otra cosa.
- **Decir cuando el caso no conviene**, aunque el cliente quiera demandar. Es
  precisamente el momento en que el consejo vale.
- **Los porcentajes son estimaciones y se marcan como tales**, no se presentan como
  cálculos.

## Lo que esta skill NO hace

- No consulta antecedentes judiciales del demandado ni verifica bienes.
- No garantiza duraciones: las estima con el conocimiento del circuito que aporte el
  usuario.
- No sustituye el criterio del abogado: lo estructura.
