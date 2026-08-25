# Vigía de cumplimiento — cookbook

Vigila el calendario de cumplimiento, el estado de los componentes del sistema y la
reevaluación anual de los umbrales de sujeto obligado.

## Arquitectura

```
vigia-de-cumplimiento-co                    read, grep, glob
  ├── lector-de-calendario-co               read, grep, glob
  ├── verificador-de-umbrales-co            read
  └── redactor-de-reporte-cumplimiento-co   read, write (solo ./salida/)
```

## Qué concede cada agente

| Agente | read | grep | glob | web_fetch | write | MCP |
|---|---|---|---|---|---|---|
| `vigia-de-cumplimiento-co` (orquestador) | ✓ | ✓ | ✓ | — | — | — |
| `lector-de-calendario-co` | ✓ | ✓ | ✓ | — | — | — |
| `verificador-de-umbrales-co` | ✓ | — | — | — | — | — |
| `redactor-de-reporte-cumplimiento-co` | ✓ | — | — | — | ✓ | — |

**Ningún agente sale a la red.** Trabaja sobre el calendario y las cifras que se le
configuren.

## La regla que define este cookbook

> **El agente no es fuente de umbrales.**

Los umbrales de SAGRILAFT y de PTEE viven en la Circular Básica Jurídica de la
Superintendencia de Sociedades y cambian por circulares externas. El agente reporta el
umbral **que tiene configurado**, marcado siempre como pendiente de verificación, y con
la fuente y la fecha de esa configuración.

Un agente que afirme un umbral con seguridad puede llevar a una empresa a implementar un
sistema que no necesita —decenas de millones— o, peor, a no implementar uno al que está
obligada.

## El barrido de enero

La corrida más importante del año: con corte a 31 de diciembre se reevalúa si la
organización cruzó algún umbral. Se hace **con el SMLMV del año nuevo**, y el reporte lo
dice explícitamente.

Una empresa que crece deja de estar exenta sin que nadie lo note. Ese es el punto ciego
que este cookbook cubre.

## Datos personales

Los seguimientos post-denuncia se reportan **por radicado**, nunca con nombres de
denunciantes ni de denunciados. Ver
[`referencias/tratamiento-de-datos.md`](../../referencias/tratamiento-de-datos.md).

## Lo que este cookbook NO hace

- No presenta reportes a la UIAF ni a la Superintendencia.
- No actualiza matrices ni dicta capacitaciones.
- No consulta listas restrictivas.
- No afirma umbrales: los reporta marcados para verificación.
