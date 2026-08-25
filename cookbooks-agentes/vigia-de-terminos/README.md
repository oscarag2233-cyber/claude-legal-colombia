# Vigía de términos — cookbook

Recalcula los términos judiciales y administrativos de los asuntos activos y avisa lo que
vence, con la norma a la vista.

## Arquitectura

```
vigia-de-terminos-co                  read, grep, glob
  ├── lector-de-registro-co           read, grep, glob
  ├── calculador-de-terminos-co       read
  └── redactor-de-alertas-co          read, write (solo ./salida/)
```

## Qué concede cada agente

| Agente | read | grep | glob | web_fetch | write | MCP |
|---|---|---|---|---|---|---|
| `vigia-de-terminos-co` (orquestador) | ✓ | ✓ | ✓ | — | — | — |
| `lector-de-registro-co` | ✓ | ✓ | ✓ | — | — | — |
| `calculador-de-terminos-co` | ✓ | — | — | — | — | — |
| `redactor-de-alertas-co` | ✓ | — | — | — | ✓ | — |

**Ningún agente de este cookbook sale a la red.** Trabaja exclusivamente sobre el registro
local: no consulta la Rama Judicial ni ningún sistema externo, porque no hay conector
disponible. Eso significa que **la calidad del reporte depende de la calidad del
registro**, y el cookbook lo dice explícitamente en cada corrida.

## Las dos reglas duras

1. **Ningún término se reporta sin la norma que lo fija.** Si el registro no la trae, el
   término va a la sección de *no calculables*, no a una fecha estimada.
2. **Si el calendario judicial del año no está cargado, el reporte lo dice en la primera
   línea.** Los conteos descuentan sábados, domingos y festivos nacionales, pero **no**
   vacancia judicial ni días no laborables del despacho.

## Franjas

| Franja | Ventana |
|---|---|
| Vencido | Ya pasó — encabeza el reporte |
| Crítico | 0-2 días hábiles |
| Urgente | 3-5 días hábiles |
| Próximo | 6-15 días hábiles |
| Horizonte | Más de 15 — solo conteo |

## Datos personales

El reporte usa **identificador de asunto, radicado o iniciales**. Nunca nombres completos
ni documentos de identidad: el reporte circula por canales de equipo. Ver
[`referencias/tratamiento-de-datos.md`](../../referencias/tratamiento-de-datos.md).

## Lo que este cookbook NO hace

- No radica, no presenta memoriales, no contesta.
- No consulta el estado electrónico de los procesos.
- No decide prioridades: las expone.
- No inventa fechas de inicio ni normas faltantes.
