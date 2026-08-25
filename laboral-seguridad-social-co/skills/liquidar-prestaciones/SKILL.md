---
name: liquidar-prestaciones
description: >
  Liquida cesantías, intereses a las cesantías, prima de servicios, vacaciones,
  indemnización por despido, sanciones moratorias y aportes, con memoria de cálculo y
  base salarial explícita. Actívela ante «liquidación de prestaciones», «cuánto le debo
  a un trabajador», «liquidar a alguien que renunció», «calcular la indemnización»,
  «sanción moratoria», «me liquidaron mal», o cuando el usuario dé fechas y salario y
  pida cifras.
---

# Liquidar prestaciones

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/laboral-seguridad-social-co/CLAUDE.md`.
Aplican los guardarraíles del perfil.

> **Advertencia de vigencia que va en toda salida de esta skill.** La **Ley 2466 de
> 2025** modificó reglas de jornada, recargos y contratación. Antes de entregar una
> liquidación, verificar qué régimen aplica al período liquidado y si hay régimen de
> transición. `[verificar vigencia, reglamentación y transición]` Las fórmulas de esta
> skill son las clásicas del CST; los **recargos y la jornada** son lo primero que hay
> que contrastar.

## Paso 1 — Los datos, antes que las fórmulas

Sin estos datos no hay liquidación. Pedirlos todos:

| Dato | Por qué importa |
|---|---|
| Fecha de ingreso y fecha de terminación | Define los días de cada concepto |
| Tipo de contrato | Fijo, indefinido, obra o labor — cambia la indemnización |
| Último salario y su composición | Básico, comisiones, horas extras, recargos, bonificaciones |
| ¿Salario variable? | La base es el **promedio** del último año o del tiempo servido |
| ¿Salario integral? | No hay cesantías, prima ni intereses separados (CST art. 132) |
| ¿Auxilio de transporte? | Se incluye en la base de cesantías y prima si el salario es hasta 2 SMLMV |
| Pagos no salariales pactados | Verificar que el pacto de exclusión salarial sea válido (art. 128 CST) |
| Forma de terminación | Renuncia, mutuo acuerdo, justa causa, sin justa causa, vencimiento del plazo |
| Vacaciones disfrutadas y pagadas | Para el saldo |
| Cesantías consignadas y anticipos | Para el saldo |
| ¿Se pagó todo el día siguiente a la terminación? | Detona el art. 65 |

**Si el salario es variable y no se tiene el histórico, detenerse.** Liquidar con el
último mes cuando el salario es variable produce una cifra equivocada en ambos sentidos.

## Paso 2 — La base salarial

La base **no es siempre el básico**. Constituye salario todo lo que recibe el trabajador
como contraprestación directa del servicio (CST art. 127): comisiones, horas extras,
recargos, porcentajes sobre ventas, viáticos permanentes en lo que corresponda a
alimentación y alojamiento.

**No constituye salario** (art. 128): lo que se recibe ocasionalmente y por mera
liberalidad, viáticos accidentales, prestaciones sociales, y **lo que las partes hayan
pactado expresamente como no salarial** — pero ese pacto tiene límites: no puede
desnaturalizar la contraprestación del servicio, y la jurisprudencia laboral lo revisa
con lupa `[verificar la línea vigente de la Sala Laboral]`.

**Auxilio de transporte:** se suma a la base de **cesantías y prima** cuando el
trabajador devenga hasta 2 SMLMV. No entra en la base de vacaciones.

## Paso 3 — Las fórmulas

*Base de 360 días al año, 30 por mes.*

### Cesantías
```
Cesantías = (Salario base mensual × días trabajados) / 360
```
Salario base: el último, o el promedio del último año si fue variable o si varió en los
últimos tres meses (CST art. 253).

### Intereses a las cesantías
```
Intereses = (Cesantías × días trabajados × 0,12) / 360
```
Se pagan a más tardar el **31 de enero** del año siguiente. La sanción por no pagarlos
es **el doble** de los intereses causados (Ley 52 de 1975).

### Prima de servicios
```
Prima = (Salario base mensual × días trabajados en el semestre) / 360
```
Un mes de salario por año, pagadero por semestres (CST art. 306, mod. Ley 1788 de 2016,
que la extendió a los trabajadores del servicio doméstico).

### Vacaciones
```
Vacaciones = (Salario base mensual × días trabajados) / 720
```
15 días hábiles de descanso por año (CST art. 186). La base **excluye** el auxilio de
transporte y, en principio, el trabajo suplementario.

### Indemnización por despido sin justa causa (CST art. 64, mod. Ley 789 de 2002 art. 28)

`[verificar si la Ley 2466 de 2025 modificó este artículo]`

| Tipo de contrato | Indemnización |
|---|---|
| **Término fijo** | El tiempo que falte para cumplir el plazo pactado |
| **Obra o labor** | El tiempo que falte para terminar la obra, **mínimo 15 días** |
| **Indefinido — salario < 10 SMLMV** | **30 días** de salario por el primer año, y **20 días** por cada año subsiguiente y proporcionalmente por fracción |
| **Indefinido — salario ≥ 10 SMLMV** | **20 días** de salario por el primer año, y **15 días** por cada año subsiguiente y proporcionalmente por fracción |

### Sanción moratoria (CST art. 65, mod. Ley 789 de 2002)

Si al terminar el contrato el empleador no paga salarios y prestaciones:

- Trabajador que devengaba **más de 1 SMLMV**: **un día de salario por cada día de
  retardo, hasta 24 meses**; a partir del mes 25, intereses moratorios a la tasa máxima
  de créditos de libre asignación certificada por la Superintendencia Financiera.
- Trabajador que devengaba **hasta 1 SMLMV**: régimen propio del artículo `[verificar]`.

**La sanción no es automática:** la jurisprudencia laboral exige valorar la **buena fe**
del empleador. Un empleador que consignó lo que consideraba debido y discutía de buena
fe una diferencia puede no ser condenado `[verificar la línea vigente]`. Decir esto
siempre: cambia la negociación.

### Sanción por no consignar cesantías (Ley 50 de 1990, art. 99 num. 3)

Un día de salario por cada día de retardo en la consignación al fondo, cuyo plazo vence
el **14 de febrero** de cada año.

## Paso 4 — Aportes y descuentos

- **Seguridad social:** salud 4%, pensión 4% a cargo del trabajador (aportes del
  empleador: 8,5% salud y 12% pensión, con las exoneraciones de la Ley 1607 de 2012
  cuando aplican) `[verificar porcentajes y exoneraciones vigentes]`.
- **Fondo de solidaridad pensional** para salarios de 4 SMLMV o más.
- **Descuentos:** solo los autorizados por la ley o por el trabajador por escrito
  (CST arts. 149-152). **No se puede descontar de la liquidación una deuda no autorizada.**
- **Retención en la fuente** sobre la indemnización cuando corresponde.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Liquidación — [trabajador] — [fecha]

### Datos
| Dato | Valor | Fuente |
|---|---|---|
| Ingreso / Retiro | | |
| Días laborados | | |
| Tipo de contrato | | |
| Salario base | $[X] | [último / promedio de N meses] |
| Auxilio de transporte incluido | [sí/no] | [porque devenga hasta 2 SMLMV] |

### Liquidación
| Concepto | Fórmula | Base | Días | Valor |
|---|---|---|---|---|
| Cesantías | (S × d)/360 | | | |
| Intereses a cesantías | (C × d × 12%)/360 | | | |
| Prima de servicios | (S × d)/360 | | | |
| Vacaciones | (S × d)/720 | | | |
| Indemnización art. 64 | | | | |
| **Subtotal** | | | | |
| (−) Descuentos autorizados | | | | |
| **NETO A PAGAR** | | | | |

### Contingencias
| Contingencia | Exposición | Probabilidad | Nota |
|---|---|---|---|
| Sanción art. 65 CST | $[día × días] hasta 24 meses | | Depende de la buena fe |
| Sanción cesantías no consignadas | | | |
| Sanción intereses (doble) | | | |

### Advertencia de vigencia
Régimen aplicado: [CST clásico / con ajustes de la Ley 2466 de 2025]
`[verificar]` — [qué falta confirmar]

### Supuestos usados
[cada supuesto, explícito]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Nunca una cifra sin memoria de cálculo.** Fórmula, base, días.
- **Nunca liquidar salario variable con el último mes.**
- **Advertir siempre sobre el art. 65** cuando el pago no se hizo al terminar: es la
  contingencia que más multiplica una liquidación pequeña.
- **Si el trabajador tiene estabilidad reforzada** (embarazo, salud, fuero sindical,
  prepensionado, denunciante de acoso), **detenerse**: la liquidación no es el problema,
  el despido lo es. Remitir a `/laboral-seguridad-social-co:terminacion-y-justa-causa`.

## Lo que esta skill NO hace

- No liquida seguridad social ante la UGPP: señala la exposición.
- No decide si un pago es o no salarial cuando hay pacto de exclusión: lo marca para
  revisión.
- No sustituye la nómina: verifica y calcula.
