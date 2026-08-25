---
name: revision-de-declaracion
description: >
  Revisa una declaración tributaria contra su soporte, identifica inconsistencias y decide
  entre corrección voluntaria, corrección provocada o defensa, con el cálculo de sanciones
  y su reducción. Actívela ante «revisa esta declaración», «me equivoqué en la
  declaración», «corregir declaración de renta o de IVA», «sanción por corrección»,
  «firmeza», «beneficio de auditoría», o antes de que la DIAN pregunte.
---

# Revisión de declaración

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/tributario-co/CLAUDE.md`.

> 🔴 **Advertencia de vigencia obligatoria en toda salida.** El Estatuto Tributario se
> modifica cada dos o tres años. La **Ley 2277 de 2022** cambió tarifas, sanciones y
> beneficios, y algunos de sus artículos fueron demandados. **Ningún término, tarifa,
> porcentaje de sanción ni UVT de esta skill se usa sin verificarlo contra el texto
> vigente y contra la doctrina de la DIAN.** `[verificar]`

## Paso 1 — 🔴 La firmeza: cuánto tiempo hay

| Situación | Firmeza |
|---|---|
| Regla general | **3 años** desde el vencimiento del plazo para declarar, o desde la presentación si fue extemporánea (ET art. 714) |
| Declaración con **saldo a favor** | 3 años desde la presentación de la solicitud de devolución o compensación |
| Contribuyentes con **pérdidas fiscales** | Término ampliado `[verificar el plazo vigente]` |
| Sujetos al régimen de **precios de transferencia** | Término ampliado `[verificar]` |
| **Beneficio de auditoría** | Firmeza reducida si se cumplen los requisitos de incremento del impuesto neto de renta y demás condiciones (ET art. 689-3 y concordantes) `[verificar vigencia, años cubiertos y porcentajes]` |

**Lo primero que se determina es si la declaración ya está en firme.** Si lo está, la DIAN
no puede modificarla y la conversación cambia por completo.

## Paso 2 — El cruce con el soporte

| Frente | Qué se revisa | Riesgo típico |
|---|---|---|
| **Ingresos** | Facturación electrónica, información exógena de terceros, extractos | Diferencia entre lo declarado y lo reportado por terceros. **La exógena es la principal fuente de requerimientos** |
| **Costos y deducciones** | Soportes, requisitos de procedencia (ET arts. 107, 771-2), pagos en efectivo (art. 771-5) | Gasto sin relación de causalidad, necesidad o proporcionalidad; factura que no cumple requisitos |
| **IVA descontable** | Facturas, oportunidad, prorrateo | Descuento improcedente por operaciones excluidas |
| **Retenciones** | Certificados, tarifas, bases | Retención practicada y no declarada |
| **Pasivos** | Soporte documental (ET art. 283) | Pasivo inexistente — es de los hallazgos más severos |
| **Activos** | Declaración de activos en el exterior, valor patrimonial | Omisión de activos |
| **Renta presuntiva / tarifas / descuentos** | | Aplicación de tarifa o descuento improcedente |

**Regla de oro:** el cruce se hace contra la **información exógena**. La DIAN ya tiene lo
que los terceros reportaron. Una revisión que no considera la exógena está mirando la
mitad del problema.

## Paso 3 — Las tres salidas

| Salida | Cuándo | Costo |
|---|---|---|
| **No hacer nada** | La declaración está bien, o está en firme | Cero |
| **Corrección voluntaria** | Hay error y todavía se puede corregir | Sanción reducida |
| **Defensa** | La posición es defendible y la DIAN podría discutirla | Costo del proceso; sanción por inexactitud si se pierde |

### Corrección que **aumenta** el impuesto o disminuye el saldo a favor (ET art. 588)

- Se presenta dentro de los **2 años** siguientes al vencimiento del plazo para declarar
  `[verificar]`, y antes de que se notifique requerimiento especial o pliego de cargos.
- **Sanción por corrección (ET art. 644):**
  - **10%** del mayor valor a pagar o del menor saldo a favor, si se corrige **antes** de
    emplazamiento o auto que ordene visita.
  - **20%**, si se corrige **después** de notificado el emplazamiento y antes del
    requerimiento especial. `[verificar]`
- Más **intereses moratorios** desde el vencimiento del plazo original (ET arts. 634 y
  635) `[verificar la tasa vigente: se calcula sobre la tasa de interés bancario corriente
  con el ajuste que fija la norma]`.

### Corrección que **disminuye** el valor a pagar o aumenta el saldo a favor (ET art. 589)

Régimen y término propios, modificados por reformas recientes. `[verificar el
procedimiento y el término vigentes]`

### Principios de graduación de sanciones (ET art. 640)

Este artículo casi nunca se invoca y casi siempre aplica:

| Supuesto | Reducción |
|---|---|
| Sanción **liquidada por el contribuyente**, sin que se haya cometido la misma conducta en los 2 años anteriores y sin sanción en firme | **50%** |
| Ídem, con antecedente en 1 año | **75%** |
| Sanción **propuesta o determinada por la DIAN**, sin antecedente en 4 años | **50%** |
| Ídem, con antecedente | **75%** |

`[verificar los supuestos exactos y las condiciones]`

Además aplican los principios de **lesividad, proporcionalidad, gradualidad y
favorabilidad**. **Solicitar expresamente la reducción del art. 640**: no se aplica de
oficio si no se pide y se acredita el cumplimiento de las condiciones.

### Otras sanciones frecuentes

| Sanción | Norma | Cuantía |
|---|---|---|
| Extemporaneidad antes de emplazamiento | ET art. 641 | **5%** por mes o fracción, sin exceder el 100% del impuesto |
| Extemporaneidad después de emplazamiento | ET art. 642 | **10%** por mes o fracción, sin exceder el 200% |
| No declarar | ET art. 643 | Porcentajes según el impuesto |
| **Inexactitud** | ET arts. 647 y 648 | **100%** de la diferencia entre el saldo a pagar determinado y el declarado; **200%** en los casos de omisión de activos o inclusión de pasivos inexistentes `[verificar]` |
| Sanción mínima | ET art. 639 | En UVT `[verificar el valor del año]` |

**La sanción por inexactitud es la que hace la diferencia económica.** Corregir
voluntariamente cuesta 10%; que la DIAN lo determine cuesta 100%.

## Paso 4 — Cuándo NO corregir

Corregir es aceptar. Hay casos en que no conviene:

- La posición es **defendible** y hay doctrina o jurisprudencia a favor.
- El punto es de **interpretación**, no de error de hecho.
- La declaración está **cerca de la firmeza** y el riesgo de requerimiento es bajo.
- Corregir un año **abre la puerta a que la DIAN revise los demás**.

**Y casos en que corregir es claramente lo correcto:** error aritmético, omisión de
ingreso reportado en exógena, pasivo sin soporte, activo omitido. En esos, la diferencia
entre 10% y 200% no admite discusión.

## Paso 5 — Riesgo penal

**Omisión de activos o inclusión de pasivos inexistentes** y **defraudación o evasión
tributaria** están tipificados en el Código Penal (arts. 434A y 434B, incorporados por
reformas recientes) `[verificar la redacción y los umbrales vigentes]`. Hay condiciones
de procedibilidad y causales de extinción por pago.

**Cuando el hallazgo cae en esos supuestos, decirlo.** No es un tema tributario más: la
estrategia cambia y hay que coordinar con defensa penal.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Revisión de declaración — [impuesto] — [período]

### 🔴 Vigencia y firmeza
Normas verificadas contra: [ ] `[verificar]`
| Punto | Valor |
|---|---|
| Vencimiento del plazo para declarar | |
| Fecha de presentación | |
| **Firmeza** | [fecha] — art. 714 — [regla aplicada] |
| ¿Ya está en firme? | |
| ¿Aplica beneficio de auditoría? | `[verificar]` |

### Hallazgos
| # | Renglón | Declarado | Soporte | Diferencia | Riesgo | Sustento |
|---|---|---|---|---|---|---|

### Cruce con exógena
| Tercero | Reportó | Declaramos | Diferencia | Explicación |
|---|---|---|---|---|

### Análisis de la salida
| Opción | Impuesto | Sanción | Intereses | Total | Riesgo residual |
|---|---|---|---|---|---|
| No corregir | | | | | |
| Corregir hoy (art. 644, 10%) | | | | | |
| Que lo determine la DIAN (inexactitud 100%) | | | | | |

### Reducción de sanciones (art. 640)
[condiciones que se cumplen y porcentaje que se solicitará]

### 🔴 Riesgo penal
[si hay omisión de activos o pasivos inexistentes por encima de los umbrales]

### Recomendación

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Ningún porcentaje de sanción, término ni UVT se afirma sin verificar.**
- **La firmeza va primero.**
- **Si hay omisión de activos o pasivos inexistentes, advertir el riesgo penal.**
- **Solicitar siempre la reducción del art. 640** cuando se cumplan las condiciones.
- **No presentar la corrección como «sin consecuencias»:** corregir es aceptar, y puede
  llamar la atención sobre otros períodos.

## Lo que esta skill NO hace

- No presenta declaraciones ni correcciones.
- No hace contabilidad ni valida cifras: trabaja con lo aportado.
- No consulta la exógena: pide que se aporte.
