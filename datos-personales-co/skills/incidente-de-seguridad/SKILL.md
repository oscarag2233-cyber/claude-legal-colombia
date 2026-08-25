---
name: incidente-de-seguridad
description: >
  Ruta de respuesta a una violación de seguridad de datos personales: contención,
  evaluación del alcance, reporte a la Superintendencia de Industria y Comercio,
  comunicación a titulares y expediente de defensa. Actívela ante «nos hackearon», «se
  filtraron datos», «ransomware», «incidente de seguridad», «brecha de datos», «un
  empleado se llevó la base de datos», «enviamos un correo a la lista equivocada», o ante
  cualquier acceso, pérdida o divulgación no autorizada de datos.
---

# Incidente de seguridad

> **Esta skill se usa bajo presión y con reloj corriendo.** Las primeras dos secciones
> son acción; el análisis viene después.

**Antes de empezar.** Leer el perfil. Si el incidente está en curso, **no esperar a tener
toda la información** para empezar la contención.

## 0 — Las primeras dos horas

| # | Acción | Nota |
|---|---|---|
| 1 | **Contener.** Cortar accesos, revocar credenciales, aislar el sistema | Antes que documentar |
| 2 | **Preservar evidencia.** No borrar logs, no reinstalar, no «limpiar» | Destruir evidencia agrava todo |
| 3 | **Activar el equipo**: jurídico, TI, seguridad, comunicaciones, alta dirección | |
| 4 | **Abrir bitácora** con hora de cada acción y decisión | Es el expediente de defensa |
| 5 | **No comunicar externamente todavía**, salvo obligación inmediata | |
| 6 | **Si hay delito**, considerar denuncia (Ley 1273 de 2009: acceso abusivo, violación de datos personales art. 269F, daño informático) | |

**Regla de la bitácora:** hora, qué se supo, quién lo supo, qué se decidió y por qué. Una
decisión razonable documentada se defiende; una decisión correcta sin documentar, no.

## 1 — ¿Es un incidente de datos personales?

| Pregunta | Efecto |
|---|---|
| ¿Hubo acceso, pérdida, alteración o divulgación **no autorizada**? | Si no, es evento de seguridad, no incidente de datos |
| ¿Involucra **datos personales**? | Si no, no aplica la Ley 1581 |
| ¿Hay **datos sensibles** o de **menores**? | Eleva gravedad y exposición sancionatoria |
| ¿Somos **responsables** o **encargados**? | El encargado reporta al responsable; el responsable reporta a la SIC |

**Incidentes que no parecen incidentes y lo son:** correo masivo con destinatarios
visibles; documento compartido con permisos abiertos; base enviada a un proveedor sin
contrato; portátil perdido sin cifrado; empleado que se lleva la base al retirarse;
papelería con datos en la basura.

## 2 — Reporte a la SIC

La Ley 1581 (art. 17 lit. n) obliga al responsable a **informar a la autoridad las
violaciones a los códigos de seguridad y los riesgos en la administración de la
información**. La SIC fijó canal y plazo por circular.

> 🔴 `[verificar plazo y canal vigentes en la circular de la SIC]` — se ha manejado un
> plazo del orden de **quince (15) días hábiles** desde la detección, por el canal
> dispuesto por la Superintendencia. **Confirmar antes de reportar.**

**Contenido típico:** identificación del responsable y su RNBD; fecha de ocurrencia y de
detección; descripción y forma de detección; causa (externa, interna, error humano, falla
técnica); categorías y volumen de datos afectados, con indicación de sensibles y menores;
número aproximado de titulares; consecuencias probables; medidas de contención con
fechas; medidas correctivas; si se comunicó a titulares; contacto para la autoridad.

**Reportar aunque falte información.** Mejor un reporte inicial completo hasta donde se
sabe, diciendo «la investigación continúa; se remitirá informe complementario», que un
reporte tardío.

## 3 — Comunicación a los titulares

La ley colombiana no trae un mandato tan detallado de notificación individual como otros
regímenes. Pero:

- El **principio de transparencia** (art. 4 lit. e) y el derecho del titular a ser
  informado sobre el uso de sus datos sostienen el deber de comunicar cuando el incidente
  puede afectarlo.
- **Cuando el riesgo es alto** —credenciales, datos financieros, salud, información que
  permita suplantación— comunicar es lo correcto y lo defendible.
- Si se decide **no** comunicar, **documentar por qué**. Esa decisión se va a revisar.

Contenido, en lenguaje claro y sin eufemismos:

```
QUÉ PASÓ: [una o dos frases sin tecnicismos]
CUÁNDO: [fecha del incidente y fecha de detección]
QUÉ INFORMACIÓN SUYA SE VIO AFECTADA: [lista concreta]
QUÉ INFORMACIÓN NO SE VIO AFECTADA: [decirlo también: es honesto y reduce la alarma]
QUÉ HEMOS HECHO: [contención y medidas]
QUÉ LE RECOMENDAMOS HACER: [pasos accionables]
DÓNDE PREGUNTAR: [canal exclusivo, con horario]
```

**Lo que no se hace:** minimizar; decir «no hay evidencia de uso indebido» como si eso
cerrara el asunto; culpar a un tercero; enterrar la información en un comunicado.

## 4 — Otros reportes que pueden proceder

| Situación | A quién | Marco |
|---|---|---|
| Delito informático | Fiscalía / CAI Virtual | Ley 1273 de 2009 |
| Vigilada financiera | Superintendencia Financiera | Riesgo operativo `[verificar]` |
| Sector salud | Supersalud | `[verificar]` |
| Servicios públicos, telecomunicaciones | Superintendencia sectorial | `[verificar]` |
| Titulares en otras jurisdicciones | Autoridad extranjera | El GDPR exige 72 horas si hay titulares en la UE `[verificar aplicabilidad]` |
| Clientes y proveedores | Según contrato | **Suelen exigir aviso en 24-48 horas: más corto que el plazo legal** |

## 5 — Exposición

| Frente | Exposición |
|---|---|
| **SIC** | Multas hasta **2.000 SMLMV**; suspensión hasta 6 meses; cierre temporal; **cierre inmediato y definitivo** de operaciones con datos sensibles (art. 23) `[verificar]` |
| **Titulares** | Responsabilidad civil por el daño; tutela por habeas data |
| **Contractual** | Indemnizaciones pactadas |
| **Penal** | Conducta dolosa interna (Ley 1273) |

**Criterios de graduación (art. 24):** dimensión del daño, beneficio obtenido,
reincidencia, resistencia u obstrucción a la investigación, renuencia a acatar órdenes, y
**reconocimiento o aceptación expresa de la infracción antes de la decisión**. Los dos
últimos explican por qué la actitud colaborativa frente a la SIC importa.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Incidente [n.º] — detectado el [fecha]

### 🔴 Relojes
| Obligación | Vence | Estado |
|---|---|---|
| Reporte a la SIC | [fecha] `[verificar plazo]` | |
| Aviso contractual a [cliente] | [fecha] | |
| Comunicación a titulares | [decidido / pendiente] | |

### Qué pasó
### Alcance
| Categoría de datos | ¿Sensible? | N.º de titulares | Sistemas |
|---|---|---|---|

### Contención
| Medida | Hora | Responsable | Estado |
|---|---|---|---|

### Reportes que proceden
### Comunicación a titulares
**Decisión:** [comunicar / no comunicar] — **Razón:** [ ]

### Exposición estimada
### Causa raíz y medidas correctivas

---
[REPORTE A LA SIC] / [COMUNICACIÓN A TITULARES]
---

### Bitácora
[cronología hora por hora]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Verificar plazo y canal vigentes de la SIC antes de reportar.** No asumirlos.
- **No borrar ni alterar evidencia**, ni siquiera para «arreglar» el sistema.
- **La decisión de no comunicar se documenta con su razón.**
- **Si hay datos sensibles o de menores comprometidos, la salida arranca por ahí.**
- **Verificación de destinatario:** el análisis jurídico es reservado; el comunicado a
  titulares no. No confundirlos.

## Lo que esta skill NO hace

- No hace análisis forense.
- No reporta por el usuario.
- No garantiza que no haya sanción: reduce la exposición y arma la defensa.
