---
name: liquidar-perjuicios
description: >
  Liquida daño emergente, lucro cesante consolidado y futuro y perjuicios inmateriales
  con las fórmulas de matemática financiera que usan los jueces colombianos, con memoria
  de cálculo completa y actualización por IPC. Actívela ante «cuánto vale el perjuicio»,
  «liquidar los daños», «lucro cesante», «perjuicio moral», «daño a la salud», «cuánto
  puedo pedir», «actualizar la indemnización», o cuando haya que ponerle cifra a un daño.
---

# Liquidar perjuicios

**Antes de empezar.** Leer el perfil y `referencias/cuantificacion-de-perjuicios.md`,
que trae los topes y las fórmulas. **Ninguna cifra sale sin memoria de cálculo.**

> **Advertencia de jurisdicción.** Los topes orientadores de perjuicio moral **no son los
> mismos** en la jurisdicción contencioso administrativa (unificación del Consejo de
> Estado de 28 de agosto de 2014, hasta 100 SMLMV) que en la ordinaria civil, donde la
> Sala Civil ha usado sus propios criterios. Fijar la jurisdicción **antes** de escoger
> el tope. `[verificar la posición vigente de cada corporación]`

## Paso 1 — Los datos

| Dato | Para qué |
|---|---|
| Fecha del hecho dañoso | Punto de partida de todo |
| Fecha de la liquidación | Todo se actualiza a esta fecha |
| Edad de la víctima al momento del hecho | Vida probable |
| Ingreso mensual acreditado | Base del lucro cesante |
| ¿Cómo se acredita el ingreso? | Contrato, nómina, declaración de renta, certificación, testimonio |
| Porcentaje de pérdida de capacidad laboral | Si hay lesión |
| Beneficiarios y parentesco | Perjuicio moral y lucro cesante en muerte |
| Gastos incurridos | Daño emergente consolidado |
| Gastos futuros previsibles | Daño emergente futuro |
| Pagos ya recibidos | SOAT, ARL, EPS, aseguradora — se descuentan |
| IPC de las fechas relevantes | Actualización |

**Si no hay ingreso acreditado**, se usa el **SMLMV** como base mínima —criterio
consolidado en la jurisprudencia colombiana para quien trabajaba sin soporte formal—
`[verificar]`. Decirlo expresamente, no aplicarlo en silencio.

## Paso 2 — Daño emergente

**Consolidado:** todo lo efectivamente gastado entre el hecho y la liquidación, con
soporte, **actualizado por IPC**:

```
Valor actualizado = Valor histórico × (IPC final / IPC de la fecha del gasto)
```

**Futuro:** lo que habrá que gastar. Requiere prueba de la necesidad futura (concepto
médico, presupuesto). Se trae a valor presente.

Rubros típicos: gastos médicos y de rehabilitación no cubiertos, medicamentos, prótesis
con su periodicidad de reemplazo, adecuación de vivienda, transporte, acompañante o
cuidador, gastos funerarios, reparación o reposición del bien, gastos de arrendamiento
sustituto.

## Paso 3 — Lucro cesante

### Renta base

```
Ra = R × (IPC final / IPC inicial)
```

Ajustes:
- **+ 25 %** por prestaciones sociales cuando la base es el salario o el SMLMV.
- **− 25 %** por gastos de subsistencia personal de la víctima, **solo en caso de
  muerte** (lo que la víctima habría consumido en sí misma no lo recibían los
  beneficiarios).
- En lesiones, la base se multiplica por el **porcentaje de pérdida de capacidad
  laboral**.

### Consolidado (desde el hecho hasta la liquidación)

```
S = Ra × [ (1 + i)^n − 1 ] / i          con i = 0,004867 mensual
```

`n` = meses transcurridos entre el hecho y la fecha de liquidación.

### Futuro (desde la liquidación hacia adelante)

```
S = Ra × [ (1 + i)^n − 1 ] / [ i × (1 + i)^n ]
```

`n` = meses del período futuro indemnizable:
- **Lesión permanente:** hasta el fin de la vida probable laboral.
- **Muerte:** la menor entre la vida probable del causante y la del beneficiario. Para
  hijos, hasta los 25 años si estudian, o 18 en otro caso `[verificar el criterio
  vigente]`.
- **Vida probable:** tablas de mortalidad de rentistas de la Superintendencia Financiera,
  Resolución 1555 de 2010 `[verificar tabla vigente]`.

**Distribución entre beneficiarios en caso de muerte:** el 50% para el cónyuge o
compañero permanente y el 50% restante entre los hijos, es un criterio usual pero no
único. `[verificar]` Decir qué criterio se aplicó.

## Paso 4 — Perjuicios inmateriales

| Rubro | Cómo se sustenta |
|---|---|
| **Perjuicio moral** | En parientes cercanos se **presume** por el parentesco: registros civiles. En otros, hay que probar el vínculo afectivo |
| **Daño a la salud** (contenciosa) / **daño a la vida de relación** (ordinaria) | Prueba de la afectación de la vida social, familiar, recreativa, sexual, deportiva. Testimonios, dictamen |
| **Daño a bienes constitucionales** | Subsidiario; preferentemente reparación no pecuniaria |

**No duplicar.** Pedir moral, daño a la vida de relación y daño a la salud por el mismo
sustrato sin diferenciarlos es la vía más rápida a que el juez recorte todo. Cada rubro
necesita su propio soporte fáctico.

**Escala orientadora en la contenciosa** (unificación de 2014): 100 / 50 / 35 / 25 / 15
SMLMV según el nivel de cercanía. `[verificar]` En la ordinaria, la Sala Civil maneja
sus propios topes.

## Paso 5 — Descuentos y compensación

Se descuenta lo ya recibido por el mismo concepto:

- **SOAT:** gastos médicos y la indemnización por muerte o incapacidad, hasta los topes.
- **ARL:** prestaciones de riesgos laborales (en culpa patronal, CST art. 216, se
  descuenta expresamente).
- **EPS:** atención cubierta.
- **Seguro de vida o de accidentes contratado por la víctima:** en principio **no** se
  descuenta, porque tiene causa distinta `[verificar]`.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Liquidación de perjuicios — [asunto] — [fecha de liquidación]

### Supuestos
| Supuesto | Valor | Fuente | Marca |
|---|---|---|---|
| Fecha del hecho | | | |
| Edad de la víctima | | | |
| Ingreso base | $[X] | [acreditado con / SMLMV por falta de prueba] | |
| Vida probable | [N] años | Res. 1555 de 2010 | `[verificar]` |
| Interés técnico | 0,004867 | | `[verificar]` |
| IPC usado | | DANE | `[verificar]` |
| Jurisdicción | [ordinaria / contenciosa] | | Determina los topes |

### Liquidación
| Rubro | Fórmula / criterio | Base | Período (n) | Valor |
|---|---|---|---|---|
| Daño emergente consolidado | histórico × IPC | | | |
| Daño emergente futuro | | | | |
| Lucro cesante consolidado | Ra×[(1+i)^n−1]/i | | | |
| Lucro cesante futuro | Ra×[(1+i)^n−1]/[i(1+i)^n] | | | |
| Perjuicio moral | [N] SMLMV [año] | | | |
| Daño a la salud / vida de relación | | | | |
| **SUBTOTAL** | | | | |
| (−) SOAT / ARL / otros pagos | | | | |
| **TOTAL** | | | | |

### Memoria de cálculo
[el desarrollo aritmético de cada fila, paso a paso]

### Soporte probatorio por rubro
| Rubro | Prueba que lo acredita | Estado |
|---|---|---|

### Advertencias
- La cifra debe **recalcularse a la fecha de radicación** (IPC y SMLMV cambian).
- El juramento estimatorio se hace sobre esta liquidación: no inflarla (CGP art. 206;
  Sentencia C-157 de 2013 `[verificar]`).

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Ninguna cifra sin memoria de cálculo.**
- **Todo SMLMV con su año.**
- **Rubro sin prueba se marca y no se suma al total principal:** va aparte, como
  «pretendido, pendiente de soporte».
- **No mezclar topes de jurisdicciones distintas.**

## Lo que esta skill NO hace

- No consulta el IPC ni el SMLMV en línea: usa lo que se le dé y marca lo que hay que
  verificar. Ver `referencias/valores-anuales.md`.
- No determina la pérdida de capacidad laboral.
- No garantiza que el juez conceda estas cifras: son la pretensión razonada.
