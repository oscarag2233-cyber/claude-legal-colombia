---
name: sagrilaft
description: >
  Estructura o audita el SAGRILAFT: política, matriz de riesgo, segmentación de factores,
  debida diligencia, señales de alerta, oficial de cumplimiento, capacitación, auditoría y
  reportes a la UIAF. Actívela ante «implementar SAGRILAFT», «matriz de riesgo LA/FT»,
  «manual SAGRILAFT», «oficial de cumplimiento», «ROS», «señales de alerta», «auditar
  nuestro sistema de prevención de lavado».
---

# SAGRILAFT

**Antes de empezar.** Correr `/cumplimiento-co:diagnostico-de-obligados`. Implementar un
sistema que no se necesita cuesta; no implementar uno que sí, cuesta más.

> 🔴 Todo lo de esta skill se contrasta contra el **Capítulo X de la Circular Básica
> Jurídica de la Superintendencia de Sociedades** vigente. `[verificar]`

## La lógica del sistema

SAGRILAFT es un **sistema de gestión de riesgo**, no un manual. La diferencia importa:
un manual se archiva; un sistema tiene ciclo. Las cuatro etapas:

```
IDENTIFICAR  →  MEDIR / EVALUAR  →  CONTROLAR  →  MONITOREAR
     ↑                                                    │
     └────────────────────────────────────────────────────┘
```

Y tres elementos que atraviesan todo: **políticas**, **procedimientos** y
**documentación**.

## Componente 1 — Política y gobierno

| Elemento | Contenido | Quién |
|---|---|---|
| **Política LA/FT/FPADM** | Aprobada por el **máximo órgano social** (asamblea o junta de socios). Debe constar en acta | Máximo órgano |
| **Manual de procedimientos** | Desarrolla la política | Representante legal / oficial |
| **Oficial de cumplimiento** | Persona natural, con las calidades que exige la circular, **inscrito ante la Superintendencia**, con autonomía e independencia y reporte directo al máximo órgano | |
| **Rol de la junta / máximo órgano** | Aprobar política, designar oficial, conocer informes | |
| **Rol del representante legal** | Proveer recursos, garantizar la implementación | |
| **Rol del revisor fiscal** | Reportar a la UIAF y a la Superintendencia lo que detecte | |

**El oficial de cumplimiento no puede ser cualquiera:** la circular fija requisitos de
idoneidad, y hay incompatibilidades (no puede ser el revisor fiscal ni pertenecer a áreas
que él mismo controla) `[verificar]`. Designarlo «además de sus funciones» a alguien sin
tiempo ni autoridad es la falla más común y la que más se sanciona.

## Componente 2 — Factores de riesgo y matriz

**Factores de riesgo** (los cuatro clásicos):

| Factor | Qué se evalúa |
|---|---|
| **Contrapartes** | Clientes, proveedores, empleados, socios, contratistas, donantes |
| **Productos y servicios** | Los que ofrece y los que adquiere la empresa |
| **Canales** | Cómo se relaciona: presencial, digital, intermediarios, distribuidores |
| **Jurisdicciones** | Dónde opera, de dónde vienen y a dónde van los recursos |

**Riesgos asociados:** reputacional, legal, operativo y de contagio.

**La matriz** cruza cada factor con sus riesgos:

| Factor / subfactor | Riesgo inherente (probabilidad × impacto) | Controles existentes | Riesgo residual | Tratamiento |
|---|---|---|---|---|

**Errores típicos de matriz:**
- Copiar la matriz de otra empresa. La matriz refleja **este** negocio.
- Calificar todo en riesgo bajo. Si nada es alto, la matriz no sirve para decidir.
- No documentar el criterio de calificación (qué es «alto» y por qué).
- No revisarla. La matriz se actualiza al menos anualmente y cada vez que cambie el
  negocio.

## Componente 3 — Debida diligencia

Ver `/cumplimiento-co:debida-diligencia-de-contraparte` para el detalle. En resumen:

| Nivel | Cuándo | Qué se hace |
|---|---|---|
| **Simplificada** | Riesgo bajo, según la matriz | Identificación básica y consulta de listas |
| **Normal** | Regla general | Identificación, verificación, beneficiario final, listas, origen de recursos |
| **Intensificada** | Riesgo alto: PEP, jurisdicciones de riesgo, operaciones inusuales, sectores sensibles | Todo lo anterior + documentación reforzada + aprobación de instancia superior + monitoreo continuo |

**Beneficiario final:** identificar a la persona natural que en última instancia posee o
controla a la contraparte. Es la obligación que más se incumple y la que más pesa en una
visita.

## Componente 4 — Señales de alerta y operaciones

| Concepto | Definición |
|---|---|
| **Operación inusual** | La que se sale del comportamiento esperado de la contraparte según su perfil y no encuentra explicación |
| **Operación sospechosa** | La inusual que, analizada, no encuentra justificación razonable |
| **ROS** | Reporte de Operación Sospechosa a la **UIAF**. **No requiere certeza ni prueba del delito**, y no constituye denuncia |

**Reglas del ROS que hay que tener claras:**

- Se envía a la UIAF por el canal dispuesto.
- **Está amparado por reserva:** quien lo reporta no incurre en responsabilidad
  (Ley 1121 de 2006, art. 42 y concordantes) `[verificar]`.
- **Prohibición de *tipping off*:** no se puede informar a la contraparte que fue
  reportada.
- **Reportar no equivale a terminar la relación**, y terminarla no sustituye el reporte.
- **La ausencia de ROS en una empresa con operaciones de riesgo es en sí misma una señal
  de alerta** para la Superintendencia.

**Señales de alerta:** el sistema debe tener un catálogo propio, derivado de la matriz, no
una lista genérica descargada de internet.

## Componente 5 — Documentación, capacitación y auditoría

| Elemento | Regla |
|---|---|
| **Conservación** | Documentos de debida diligencia y de operaciones, por el término que fije la circular `[verificar]`, y en todo caso conforme al C.Co. art. 28 y 60 |
| **Capacitación** | Anual, a todo el personal, con **registro de asistencia y evaluación**. Sin evidencia, no ocurrió |
| **Auditoría** | Del sistema, no de la contabilidad. Independiente. Con plan de acción sobre los hallazgos |
| **Informes del oficial** | Periódicos al máximo órgano, con constancia en acta |

## Auditoría del sistema — lista de verificación

Cuando la skill se usa para auditar, se recorre esto:

| # | Elemento | Existe | Vigente | Evidencia | Hallazgo |
|---|---|---|---|---|---|
| 1 | Política aprobada por el máximo órgano, con acta | | | | |
| 2 | Manual actualizado | | | | |
| 3 | Oficial designado e **inscrito** ante la Superintendencia | | | | |
| 4 | Matriz de riesgo propia y actualizada | | | | |
| 5 | Metodología de calificación documentada | | | | |
| 6 | Procedimiento de debida diligencia por nivel | | | | |
| 7 | Identificación de **beneficiario final** | | | | |
| 8 | Consulta de listas restrictivas, con evidencia | | | | |
| 9 | Catálogo propio de señales de alerta | | | | |
| 10 | Procedimiento de análisis de operaciones inusuales | | | | |
| 11 | Registro de operaciones inusuales analizadas | | | | |
| 12 | ROS enviados y su trazabilidad | | | | |
| 13 | Capacitación anual con registro | | | | |
| 14 | Auditoría del sistema y plan de acción | | | | |
| 15 | Informes del oficial al máximo órgano, en actas | | | | |
| 16 | Conservación documental | | | | |
| 17 | Tratamiento de datos personales conforme a la Ley 1581 | | | | |

**El punto 17 se olvida siempre:** la debida diligencia trata datos personales, muchas
veces sensibles (condenas, investigaciones). Necesita base de legitimación, finalidad y
seguridad. Ver `/datos-personales-co:evaluacion-de-tratamiento`.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## SAGRILAFT — [empresa] — [implementación / auditoría]

### 🔴 Vigencia
Circular consultada: [ ] `[verificar]`

### Estado del sistema
| Componente | Estado | Brecha | Severidad | Plazo |
|---|---|---|---|---|

### Matriz de riesgo
[la matriz, o los hallazgos sobre la existente]

### 🔴 Hallazgos críticos
| Hallazgo | Consecuencia | Corrección | Responsable | Plazo |
|---|---|---|---|---|

### Plan de implementación / remediación
| Fase | Entregable | Responsable | Plazo |
|---|---|---|---|

---
[POLÍTICA / MANUAL / PROCEDIMIENTO, según lo pedido]
---

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **No entregar una matriz genérica.** Si no hay información del negocio para
  construirla, pedirla.
- **La política sin acta del máximo órgano no cumple**, por buena que sea.
- **Nunca sugerir informar a la contraparte que fue reportada** (*tipping off*).
- **El ROS no requiere certeza:** corregir esa creencia cada vez que aparezca, porque es
  la razón por la que muchas empresas no reportan.
- **Advertir sobre el tratamiento de datos** en toda debida diligencia.

## Lo que esta skill NO hace

- No reporta a la UIAF.
- No consulta listas restrictivas.
- No sustituye la auditoría independiente ni el criterio del oficial de cumplimiento.
