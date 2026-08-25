---
name: garantia-y-calidad
description: >
  Determina si hay incumplimiento de la garantía legal, quién responde solidariamente y
  cuál es el remedio que corresponde pedir, bajo el Estatuto del Consumidor. Actívela ante
  «me vendieron un producto defectuoso», «no me quieren cambiar el producto», «garantía
  legal», «el carro salió malo», «reclamo al proveedor», «calidad e idoneidad», «me dicen
  que la garantía no cubre eso».
---

# Garantía y calidad

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/consumidor-competencia-co/CLAUDE.md`.
Determinar el lado: **consumidor** o **productor/proveedor**.

## Paso 1 — ¿Hay relación de consumo?

El Estatuto del Consumidor (**Ley 1480 de 2011**) solo aplica si hay **consumidor**:
persona natural o jurídica que adquiere, disfruta o utiliza un producto para la
satisfacción de una **necesidad propia, privada, familiar o doméstica y empresarial
cuando no esté ligada intrínsecamente a su actividad económica** (art. 5 num. 3).

| Escenario | ¿Aplica la Ley 1480? |
|---|---|
| Persona compra un electrodoméstico | Sí |
| Empresa compra computadores para su administración | Sí — no están ligados intrínsecamente a su actividad |
| Panadería compra un horno industrial | **No** — es insumo de su actividad económica. Va por régimen civil y mercantil |
| Empresa compra materia prima | No |

**Si no hay relación de consumo, el análisis cambia de plugin:** ver
`/contratos-comercial-co:incumplimiento-y-remedios` y las acciones edilicias del Código
Civil.

## Paso 2 — Los tres deberes que se pueden incumplir

| Deber | Contenido | Norma |
|---|---|---|
| **Calidad e idoneidad** | El producto debe servir para lo que se ofreció y cumplir las condiciones ofrecidas | Arts. 6 y 7 |
| **Garantía legal** | Obligación **a cargo de todo productor y proveedor** de responder por la calidad, idoneidad, seguridad y buen estado y funcionamiento | Art. 7 |
| **Seguridad** | El producto no debe causar daño en condiciones normales de uso | Arts. 19-22 |

**La garantía legal es de orden público:** existe aunque no se pacte, no se puede
renunciar, y **no se puede limitar por contrato**. Cualquier cláusula que la excluya es
ineficaz (art. 43 num. 1).

## Paso 3 — El término de la garantía (art. 8)

| Supuesto | Término |
|---|---|
| El que fije la ley o la autoridad competente | Ese |
| A falta de este, el que señale el productor | Ese |
| Si no se señaló ninguno | **1 año** para productos nuevos `[verificar]` |
| Bienes **usados** con menos de 1 año de uso | Puede pactarse un término menor, con información expresa `[verificar]` |
| **Prestación de servicios** | El término que corresponda; en servicios que suponen la entrega de un bien, se aplica la garantía sobre el bien |
| **Bienes inmuebles** | Estabilidad de la obra: **10 años**; acabados: **1 año** `[verificar]` |
| **Servicios que suponen la entrega de un bien reparado** | 3 meses sobre la reparación `[verificar]` |

**El término se suspende mientras el producto está en reparación**, y si se cambia el
producto o la pieza, la garantía se renueva sobre lo cambiado.

## Paso 4 — Quién responde

> **Productor y proveedor responden SOLIDARIAMENTE** ante el consumidor por la garantía
> legal (art. 10).

Esto es lo que más se discute en la práctica y lo que decide contra quién se reclama:

- El consumidor puede reclamar **al vendedor** aunque el defecto sea de fábrica.
- «Reclame al fabricante» **no es una respuesta válida** del vendedor.
- El importador responde como productor.
- Entre ellos pueden repetir después; eso no es problema del consumidor.

## Paso 5 — Efectividad de la garantía (art. 11)

Ante un incumplimiento, el consumidor tiene derecho a:

| # | Remedio | Cuándo |
|---|---|---|
| 1 | **Reparación totalmente gratuita** de los defectos, y las prestaciones a cargo de quien otorga la garantía | Regla general |
| 2 | **Cambio del bien por otro igual o de las mismas características**, o **devolución del precio pagado** | Cuando el producto **se repitió la falla**, o cuando la reparación no es posible, o no se hizo en el término |
| 3 | **Devolución del dinero** | En los mismos supuestos |
| 4 | Suministro de repuestos y de servicio técnico | |
| 5 | En servicios: prestar de nuevo el servicio o devolver el precio | |

**Regla operativa (art. 11 num. 3):** si el producto se repara y **vuelve a fallar por la
misma causa**, procede el cambio o la devolución del dinero. Esta es la regla que más
sirve al consumidor y la que los proveedores más resisten.

**Gastos de transporte y envío:** son a cargo de quien otorga la garantía.

**Término para hacer efectiva la garantía:** el proveedor debe resolver la reclamación en
un plazo corto `[verificar el término vigente del reglamento]`; el silencio se interpreta
en contra.

## Paso 6 — Exoneraciones (art. 16)

El productor o proveedor **solo** se exonera probando:

1. **Fuerza mayor o caso fortuito.**
2. **Hecho de un tercero.**
3. **Uso indebido del bien por el consumidor.**
4. Que el consumidor **no atendió las instrucciones** de instalación, uso o mantenimiento
   indicadas en el manual y en la garantía.

**La carga de la prueba de la exoneración es del productor o proveedor.** El consumidor no
tiene que probar el origen del defecto: le basta acreditar que el producto no sirve para
lo ofrecido.

**Consecuencia práctica para el proveedor:** un peritaje que diga «mal uso» sin sustento
no exonera. Y para el consumidor: cuando le dicen «usted lo dañó», la respuesta es «acredítelo».

## Paso 7 — Producto defectuoso y daño (arts. 19-22)

Es un régimen **distinto** de la garantía: aquí no se reclama el producto, se reclama el
**daño que el producto causó**.

| Punto | Regla |
|---|---|
| Naturaleza | **Responsabilidad objetiva y solidaria** del productor y del expendedor |
| Qué se prueba | El **defecto**, el **daño** y el **nexo causal** — no la culpa |
| Qué se indemniza | Muerte o lesiones, y daño a otros bienes distintos del producto defectuoso |
| Exoneración | Fuerza mayor, culpa exclusiva de la víctima, hecho de un tercero, que no se haya puesto en circulación, que el defecto sea consecuencia de normas imperativas `[verificar]` |

**Si hubo daño personal o a otros bienes, no se queda en garantía:** se acumula con la
acción de responsabilidad. Ver `/responsabilidad-civil-co:analisis-de-responsabilidad`.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Garantía — [producto o servicio] — [proveedor]

**Lado:** [consumidor / productor o proveedor]

### ¿Hay relación de consumo?
[Sí / No — y a qué régimen va si no]

### Los hechos
| Dato | Contenido |
|---|---|
| Producto y fecha de compra | |
| Precio | |
| Vendedor / productor | |
| Falla presentada | |
| Fecha de la falla | |
| Reclamaciones previas | |
| ¿Hubo reparación anterior por la misma causa? | **Decisivo** |

### Término de la garantía
| Punto | Valor |
|---|---|
| Término aplicable | [ ] — art. 8 |
| ¿Está vigente? | |
| Suspensiones por reparación | |

### Remedio que corresponde
**[Reparación / Cambio / Devolución del dinero]** — art. 11 num. [ ] — porque [ ]

### Responsables solidarios
| Responsable | Título | Solvencia |
|---|---|---|

### Exoneraciones alegadas o previsibles
| Causal | ¿Está probada? | Quién carga la prueba |
|---|---|---|

### ¿Hubo daño más allá del producto?
[Si sí → acumular acción por producto defectuoso, arts. 19-22]

### Siguiente paso
[Reclamación directa → demanda de protección al consumidor →
`/consumidor-competencia-co:demanda-de-proteccion-al-consumidor`]

---
[RECLAMACIÓN AL PROVEEDOR / RESPUESTA A LA RECLAMACIÓN]
---

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **La garantía legal no se puede excluir por contrato.** Rechazar cualquier cláusula que
  lo intente.
- **«Reclame al fabricante» no es respuesta.** La solidaridad del art. 10 es del
  consumidor, no del proveedor.
- **La carga de probar la exoneración es del proveedor:** decirlo siempre.
- **Si hubo daño personal, cambiar de marco** y no dejarlo en garantía.
- **Verificar la caducidad de la acción** antes de recomendar demandar: el año siguiente a
  la terminación de la garantía `[verificar]`.

## Lo que esta skill NO hace

- No hace peritajes técnicos.
- No radica reclamaciones ni demandas.
- No fija el término de garantía cuando el productor no lo señaló y hay norma sectorial:
  remite a verificarla.
