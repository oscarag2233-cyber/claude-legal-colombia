# Cuantificación de perjuicios en Colombia

Referencia compartida para responsabilidad civil, del Estado, laboral y penal
(incidente de reparación integral).

> Todos los topes y fórmulas de este archivo se marcan `[verificar vigencia]`. Las
> escalas de unificación se ajustan y el SMLMV cambia cada año.

## Tipología del daño

### Perjuicios materiales

| Rubro | Contenido |
|---|---|
| **Daño emergente** | Erogaciones efectuadas o que deban efectuarse como consecuencia del daño (gastos médicos, reparaciones, funerarios, honorarios). Consolidado y futuro |
| **Lucro cesante** | Ganancia o provecho que deja de percibirse. Consolidado (desde el hecho hasta la sentencia) y futuro (desde la sentencia hacia adelante) |

### Perjuicios inmateriales

| Rubro | Jurisdicción | Tope orientador |
|---|---|---|
| **Perjuicio moral** | Contenciosa | Hasta **100 SMLMV** por víctima en muerte, nivel 1; escala descendente por cercanía (100 / 50 / 35 / 25 / 15 SMLMV) — Consejo de Estado, Sección Tercera, sentencias de unificación de **28 de agosto de 2014** `[verificar]` |
| **Perjuicio moral** | Civil (CSJ) | La Sala Civil ha usado topes orientadores propios; **no** son los mismos de lo contencioso `[verificar la posición vigente]` |
| **Daño a la salud** | Contenciosa (lesiones personales) | Hasta **100 SMLMV**; hasta **400 SMLMV** en casos de gravedad excepcional debidamente motivados `[verificar]` |
| **Daño a bienes o derechos constitucional y convencionalmente amparados** | Contenciosa | Hasta **100 SMLMV**, subsidiario y de reparación preferentemente no pecuniaria `[verificar]` |
| **Daño a la vida de relación / alteración de las condiciones de existencia** | Civil | Categoría propia de la jurisdicción ordinaria; no confundir con «daño a la salud» `[verificar]` |
| **Privación injusta de la libertad** | Contenciosa | Escala en SMLMV según duración de la privación `[verificar unificación vigente]` |

**No duplicar rubros.** Daño a la salud, daño a la vida de relación y perjuicio moral
responden a bienes jurídicos distintos, pero pedir los tres por el mismo hecho sin
diferenciar el sustrato probatorio es la vía más rápida a que el juez recorte todo.

## Fórmulas de lucro cesante (matemática financiera del Consejo de Estado)

Interés puro o técnico: **i = 0,004867** mensual (6% anual). `[verificar]`

**Renta actualizada:**

```
Ra = R × (IPC final / IPC inicial)
```

**Ajustes usuales sobre la renta:**
- `+ 25 %` por prestaciones sociales cuando la base es el salario o el SMLMV.
- `− 25 %` por gastos de subsistencia personal de la víctima directa (en muerte).

**Lucro cesante consolidado (vencido):**

```
S = Ra × [ (1 + i)^n − 1 ] / i
```

**Lucro cesante futuro (anticipado):**

```
S = Ra × [ (1 + i)^n − 1 ] / [ i × (1 + i)^n ]
```

donde `n` = número de meses del período respectivo.

**Vida probable:** tablas de mortalidad de rentistas de la Superintendencia
Financiera (Resolución 1555 de 2010). `[verificar tabla vigente]` En lesiones se usa
la vida probable de la víctima; en muerte, la menor entre la del causante y la del
beneficiario.

## Reglas de método

1. **Cada rubro se prueba por separado.** El perjuicio moral en parientes cercanos se
   presume por el parentesco (registro civil); todo lo demás se prueba.
2. **Actualizar siempre a la fecha de la liquidación** con IPC del DANE.
3. **Indicar el SMLMV usado y su año.** Ver `referencias/valores-anuales.md`.
4. **Descontar lo ya pagado** por SOAT, ARL, EPS o aseguradora, cuando corresponda,
   para evitar enriquecimiento sin causa y la objeción de compensatio lucri cum damno.
5. **Nunca entregar una cifra sin la memoria de cálculo**: base, fórmula, `n`, `i`,
   fuente del IPC y de la vida probable.

## Salida obligatoria

```
| Rubro | Base | Fórmula / criterio | Período | Valor | Prueba que lo soporta | Fuente del criterio |
|---|---|---|---|---|---|---|
```
Cerrar con: `TOTAL` + `[verificar] la cifra debe recalcularse a la fecha de radicación`.
