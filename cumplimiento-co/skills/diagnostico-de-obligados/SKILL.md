---
name: diagnostico-de-obligados
description: >
  Determina si la empresa es sujeto obligado a implementar SAGRILAFT, PTEE, ambos o
  ninguno, con los umbrales y el año de corte que corresponden, e identifica los demás
  regímenes de cumplimiento que puedan aplicar. Actívela ante «¿tenemos que implementar
  SAGRILAFT?», «¿nos aplica el PTEE?», «umbrales de la Superintendencia de Sociedades»,
  «somos sujeto obligado», «autodiagnóstico de cumplimiento», o antes de invertir en un
  sistema que quizá no se necesita.
---

# Diagnóstico de obligados

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/cumplimiento-co/CLAUDE.md`.

> 🔴 **Advertencia de vigencia que va en toda salida de esta skill.** Los umbrales, los
> sectores y los plazos de SAGRILAFT y PTEE están en la **Circular Básica Jurídica de la
> Superintendencia de Sociedades** (Capítulos X y XIII), que se modifica con frecuencia
> por circulares externas. **Ningún umbral de esta skill se usa sin verificarlo contra la
> circular vigente.** `[verificar]`

## Paso 1 — ¿Quién es la autoridad?

El régimen de cumplimiento depende de **quién vigila a la entidad**:

| Autoridad | Régimen | Norma |
|---|---|---|
| **Superintendencia de Sociedades** | **SAGRILAFT** (Cap. X) y **PTEE** (Cap. XIII) | Circular Básica Jurídica |
| **Superintendencia Financiera** | **SARLAFT** | Circular Básica Jurídica Financiera, Parte I, Título IV, Cap. IV `[verificar]` |
| **Superintendencia de Salud, de Servicios Públicos, de Vigilancia, de Transporte, de Economía Solidaria** | Regímenes sectoriales propios | `[verificar el aplicable]` |
| **DIAN** (usuarios aduaneros) | Régimen propio | |
| **Coljuegos, Supersolidaria, etc.** | | |

**Primera pregunta, siempre:** ¿quién vigila a esta empresa? Aplicar el Capítulo X a una
entidad vigilada por la Superintendencia Financiera es un error de partida.

## Paso 2 — SAGRILAFT (Capítulo X)

**Qué es:** Sistema de Autocontrol y Gestión del Riesgo Integral de Lavado de Activos,
Financiación del Terrorismo y Financiación de la Proliferación de Armas de Destrucción
Masiva (LA/FT/FPADM).

**Criterios de obligación** `[verificar todos contra la circular vigente]`:

| Criterio | Contenido |
|---|---|
| **Umbral general** | Sociedades vigiladas, controladas o inspeccionadas por la Superintendencia de Sociedades que, a 31 de diciembre del año inmediatamente anterior, hayan obtenido **ingresos totales** o tengan **activos totales** iguales o superiores a determinado número de SMLMV |
| **Sectores de mayor riesgo** | Umbral **menor** para actividades específicas: agentes inmobiliarios, comercialización de metales preciosos y piedras preciosas, servicios contables, servicios jurídicos, activos virtuales, construcción, comercio de vehículos, entre otros |
| **Régimen de medidas mínimas** | Empresas que no alcanzan el umbral del sistema completo pero sí uno inferior deben adoptar **medidas mínimas** |
| **Fecha de corte** | 31 de diciembre del año anterior |
| **Plazo de implementación** | El que fije la circular, contado desde que se supera el umbral |

**Componentes mínimos del sistema:** política aprobada por el máximo órgano social;
**oficial de cumplimiento** inscrito ante la Superintendencia; manual; matriz de riesgo
con identificación, medición, control y monitoreo; **debida diligencia** de contrapartes;
señales de alerta; conservación de documentos; capacitación; auditoría; **reporte de
operaciones sospechosas (ROS) a la UIAF**.

## Paso 3 — PTEE (Capítulo XIII)

**Qué es:** Programa de Transparencia y Ética Empresarial, orientado a prevenir el
**soborno transnacional** y otros actos de corrupción.

**Criterios de obligación** `[verificar]`:

| Criterio | Contenido |
|---|---|
| **Negocios o transacciones internacionales** | Haber realizado, en el año anterior, negocios o transacciones internacionales por un monto igual o superior a determinado número de SMLMV |
| **Umbral de tamaño** | Ingresos totales o activos por encima del umbral fijado |
| **Sectores específicos** | Reglas propias para determinados sectores `[verificar]` |
| **Ley 2195 de 2022** | Amplió los supuestos de programas de transparencia y ética empresarial y la responsabilidad administrativa de las personas jurídicas `[verificar el alcance]` |

**Componentes mínimos:** política aprobada por el máximo órgano; **oficial de
cumplimiento**; manual; evaluación de riesgos de corrupción; debida diligencia orientada
a terceros (intermediarios, agentes, distribuidores, socios de negocio); **canal de
denuncias** con protección al denunciante; capacitación; auditoría; procedimiento de
investigación interna.

**Se puede tener un solo oficial de cumplimiento y un sistema integrado** que atienda
ambos capítulos, si la empresa está obligada a los dos. La circular lo permite en las
condiciones que fija `[verificar]`.

## Paso 4 — Otros regímenes que pueden aplicar

| Régimen | Cuándo | Norma |
|---|---|---|
| **Responsabilidad administrativa por soborno transnacional** | La persona jurídica cuyos empleados, administradores, asociados o contratistas den, ofrezcan o prometan dádivas a un servidor público extranjero | **Ley 1778 de 2016**; competencia de la Superintendencia de Sociedades. Sanciones: multas hasta **200.000 SMLMV**, inhabilidad para contratar con el Estado hasta 20 años, publicación de la decisión, prohibición de recibir incentivos del Estado `[verificar]` |
| **Responsabilidad de personas jurídicas por corrupción** | Ley 2195 de 2022 amplió el régimen | `[verificar alcance y procedimiento]` |
| **Protección de datos** | Toda debida diligencia trata datos personales | Ley 1581 de 2012 — ver `/datos-personales-co:evaluacion-de-tratamiento` |
| **Competencia** | Programas de cumplimiento en libre competencia | Ley 1340 de 2009 — ver `/consumidor-competencia-co:practicas-restrictivas` |
| **Seguridad y salud en el trabajo** | SG-SST | Decreto 1072 de 2015 |
| **Contratación con el Estado** | Inhabilidades y transparencia | Ley 1474 de 2011 |

## Paso 5 — Qué pasa si se es obligado y no se implementa

| Consecuencia | Alcance |
|---|---|
| **Sanciones de la Superintendencia de Sociedades** | Multas a la sociedad y **a los administradores y al revisor fiscal**, personalmente |
| **Responsabilidad de administradores** | Ley 222 de 1995, art. 23 num. 2: velar por el estricto cumplimiento de las disposiciones legales |
| **Exposición penal** | Omisión de control, lavado de activos por omisión, según el caso |
| **Contratación** | Exclusión de procesos que exigen programas de cumplimiento |
| **Bancaria** | Desvinculación de relaciones financieras |
| **Reputacional y comercial** | Contrapartes que exigen el sistema como requisito |

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Diagnóstico de obligados — [empresa] — corte a 31-12-[año]

### 🔴 Advertencia de vigencia
Los umbrales aplicados provienen de [circular consultada o «conocimiento del modelo —
verificar»]. **Confirmar contra la Circular Básica Jurídica vigente antes de decidir.**

### Datos de la empresa
| Dato | Valor | Fuente |
|---|---|---|
| Autoridad de vigilancia | | |
| Situación: vigilada / controlada / inspeccionada | | |
| Ingresos totales a 31-12-[año] | $[X] = [N] SMLMV [año] | Estados financieros |
| Activos totales a 31-12-[año] | $[X] = [N] SMLMV [año] | Estados financieros |
| Actividad económica (CIIU) | | RUT |
| ¿Sector de mayor riesgo? | | |
| Transacciones internacionales del año | $[X] = [N] SMLMV | |
| ¿Contrata con el Estado? | | |

### Veredicto
| Régimen | ¿Obligado? | Umbral aplicado | Plazo de implementación |
|---|---|---|---|
| SAGRILAFT completo | | | |
| SAGRILAFT — medidas mínimas | | | |
| PTEE | | | |
| Ley 1778 (soborno transnacional) | Aplica a toda persona jurídica en los supuestos de la ley | — | — |
| Otros | | | |

### Si es obligado — qué hay que tener
| Componente | Existe | Brecha | Prioridad |
|---|---|---|---|

### Si no es obligado
[Qué conviene tener de todos modos y por qué: exigencias de contrapartes, bancos,
licitaciones, y el deber general de diligencia de los administradores.]

### Ruta y costos
| Fase | Entregable | Plazo | Responsable |
|---|---|---|---|

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Ningún umbral se afirma sin verificar la circular vigente.** Es el dato que más
  cambia y el que decide una inversión de decenas de millones.
- **Los SMLMV van con su año.** Un umbral de 40.000 SMLMV es una cifra distinta cada año.
- **Si la empresa está vigilada por otra superintendencia, decirlo antes de seguir.**
- **La Ley 1778 aplica sin umbral:** no decir «no somos obligados» cuando la empresa tiene
  operaciones con funcionarios públicos extranjeros.

## Lo que esta skill NO hace

- No implementa los sistemas — para eso están `/cumplimiento-co:sagrilaft` y
  `/cumplimiento-co:ptee`.
- No verifica cifras contables: usa las que se le aporten.
- No inscribe oficiales de cumplimiento ante la Superintendencia.
