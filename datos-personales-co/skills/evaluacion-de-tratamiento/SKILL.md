---
name: evaluacion-de-tratamiento
description: >
  Mapea una actividad de tratamiento de datos personales y determina el rol (responsable
  o encargado), la base de legitimación, si hay datos sensibles o de menores, los riesgos
  y las obligaciones que se activan bajo la Ley 1581 de 2012. Actívela ante «vamos a
  recoger datos», «¿podemos usar estos datos?», «¿somos responsables o encargados?»,
  «evaluación de tratamiento», «análisis de impacto de privacidad», «esto cumple con
  habeas data», o antes de lanzar cualquier producto o proceso que trate datos.
---

# Evaluación de tratamiento

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/datos-personales-co/CLAUDE.md`.
Aplican los guardarraíles del perfil.

## Paso 1 — ¿Aplica la Ley 1581?

| Pregunta | Efecto |
|---|---|
| ¿Hay **datos personales**? (cualquier información vinculada o que pueda asociarse a personas naturales determinadas o determinables) | Si no, no aplica el régimen |
| ¿El responsable está **domiciliado en Colombia** o le aplica la ley colombiana por tratado? | Ámbito territorial (art. 2) |
| ¿Es una de las **excepciones del art. 2**? (bases personales o domésticas; inteligencia y contrainteligencia; información periodística; bases de datos de la Ley 1266; datos de censos) | Régimen distinto o exclusión |
| ¿Es **dato financiero, crediticio o comercial**? | Aplica la **Ley 1266 de 2008** (mod. Ley 2157 de 2021) como régimen especial. Ver `/datos-personales-co:habeas-data-financiero` |

**Dato personal ≠ dato identificado.** Un correo corporativo, una IP con otros datos, un
identificador de dispositivo o un dato seudonimizado reversible **son datos personales**.

## Paso 2 — El rol

Esta es la determinación que más se equivoca y de la que dependen todas las obligaciones.

| Rol | Definición (art. 3) | Señal práctica |
|---|---|---|
| **Responsable** | Decide sobre la base de datos y el tratamiento | Define para qué y cómo se usan los datos |
| **Encargado** | Realiza el tratamiento **por cuenta del responsable** | Ejecuta instrucciones; no puede usarlos para fines propios |

**Se puede ser responsable de unos datos y encargado de otros en la misma operación.**
Mapearlo por flujo, no por empresa.

| Obligación | Responsable (art. 17) | Encargado (art. 18) |
|---|---|---|
| Obtener autorización y conservar prueba | ✓ | |
| Informar la finalidad y los derechos | ✓ | |
| Política de tratamiento | ✓ | |
| Atender consultas y reclamos | ✓ | ✓ (los que reciba) |
| Garantizar seguridad | ✓ | ✓ |
| Actualizar, rectificar, suprimir | ✓ | ✓ (bajo instrucción) |
| Registro Nacional de Bases de Datos | ✓ | |
| Informar incidentes a la SIC | ✓ | Informar al responsable |
| Tratar solo bajo instrucciones | | ✓ |

## Paso 3 — La base de legitimación

**La regla es la autorización previa, expresa e informada del titular** (art. 9). No
hay un catálogo de bases alternativas como en otros regímenes: en Colombia la
autorización es el eje.

**Casos en que no se requiere autorización (art. 10):**

1. Información requerida por **entidad pública o administrativa** en ejercicio de sus
   funciones legales, o por orden judicial.
2. **Datos de naturaleza pública.**
3. Casos de **urgencia médica o sanitaria**.
4. Tratamiento autorizado por la ley para **fines históricos, estadísticos o
   científicos**.
5. Datos relacionados con el **Registro Civil** de las personas.

**Requisitos de la autorización:**
- **Previa**, **expresa** e **informada** — el titular debe conocer la finalidad.
- **Prueba de la autorización:** el responsable debe poder demostrarla (Decreto 1074).
  Casilla premarcada, silencio o continuación de la navegación **no son autorización
  válida**.
- **Autorización para datos sensibles** exige advertir que **no está obligado** a
  autorizar el tratamiento de datos sensibles.
- **Revocable.**

## Paso 4 — Datos sensibles y de menores

**Datos sensibles (art. 5):** los que afectan la intimidad o cuyo uso indebido puede
generar discriminación — origen racial o étnico, orientación política, convicciones
religiosas o filosóficas, pertenencia a sindicatos u organizaciones sociales o de
derechos humanos, datos de **salud**, de **vida sexual** y **biométricos**.

- **Prohibido su tratamiento**, salvo las excepciones del art. 6: consentimiento
  explícito (advirtiendo que no está obligado), interés vital del titular incapacitado,
  tratamiento por entidades sin ánimo de lucro respecto de sus miembros, datos
  necesarios para el reconocimiento de un derecho en un proceso judicial, o finalidad
  histórica/estadística/científica con medidas de supresión de identidad.
- **Ninguna actividad puede condicionarse a que el titular entregue datos sensibles**
  (art. 6 par.).

**Menores (art. 7):** el tratamiento está prohibido salvo cuando se trate de datos de
naturaleza pública y cuando responda al **interés superior del niño** y asegure el
respeto de sus derechos fundamentales. Se requiere autorización del representante legal,
con **el niño ejerciendo su derecho a ser escuchado**. `[verificar la línea
constitucional vigente]`

**El tratamiento de datos biométricos** (huella, rostro, voz) es sensible. Un sistema de
control de acceso o de asistencia con huella activa todo el régimen reforzado, y hay que
ofrecer alternativa.

## Paso 5 — Los principios como lista de chequeo (art. 4)

| Principio | Pregunta operativa |
|---|---|
| **Legalidad** | ¿Hay norma o autorización que soporte el tratamiento? |
| **Finalidad** | ¿La finalidad es legítima, y se le informó al titular en términos comprensibles? |
| **Libertad** | ¿El titular pudo decidir sin coacción y sin que se le condicionara un servicio? |
| **Veracidad o calidad** | ¿Los datos son veraces, completos, exactos, actualizados y comprobables? |
| **Transparencia** | ¿El titular puede saber qué datos suyos existen? |
| **Acceso y circulación restringida** | ¿Solo acceden quienes deben? ¿No están disponibles en internet salvo acceso técnicamente controlable? |
| **Seguridad** | ¿Hay medidas técnicas, humanas y administrativas? |
| **Confidencialidad** | ¿Todos los que intervienen están obligados a reserva, incluso después de terminar la relación? |

**Minimización:** aunque no está enunciada con ese nombre, la finalidad y la calidad la
imponen. Preguntar siempre: **¿todos estos campos son necesarios para la finalidad?**
Recoger la cédula «por si acaso» es una infracción esperando ocurrir.

## Paso 6 — Obligaciones que se activan

| Si… | Entonces… |
|---|---|
| Es responsable | Política de tratamiento + aviso de privacidad + canal de atención |
| Cumple los criterios del RNBD | Registro de las bases ante la SIC `[verificar umbral vigente]` |
| Contrata a un tercero que trata datos por su cuenta | Contrato de transmisión con las cláusulas del Decreto 1074, art. 2.2.2.25.5.2 `[verificar]` |
| Los datos salen del país | Ver `/datos-personales-co:transferencia-internacional` |
| Hay datos sensibles | Autorización reforzada, medidas de seguridad adicionales, justificación de necesidad |
| Hay decisiones automatizadas o perfilamiento | Informarlo en la finalidad; evaluar impacto en derechos. Ver `/gobernanza-ia-co:evaluacion-de-impacto-ia` |
| Hay una violación de seguridad | Ver `/datos-personales-co:incidente-de-seguridad` |

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Evaluación de tratamiento — [actividad]

### Semáforo
**[✅ PUEDE PROCEDER / 🟡 PUEDE PROCEDER CON CONDICIONES / 🔴 NO PUEDE PROCEDER COMO ESTÁ]**

### Mapa del tratamiento
| Elemento | Detalle |
|---|---|
| Finalidad declarada | |
| Categorías de datos | |
| ¿Hay sensibles? | [cuáles] |
| ¿Hay menores? | |
| Titulares | |
| Origen de los datos | |
| Nuestro rol | responsable / encargado / mixto |
| Terceros que acceden | [rol de cada uno] |
| ¿Salen del país? | [a dónde] |
| Tiempo de conservación | |
| Decisiones automatizadas | |

### Base de legitimación
[autorización — cómo se obtiene y cómo se prueba / excepción del art. 10 — cuál]

### Principios
[la tabla, con ✅/⚠️/🔴 en cada uno y la razón]

### Minimización
| Campo recogido | ¿Necesario para la finalidad? | Recomendación |
|---|---|---|

### 🔴 Condiciones para proceder
1. [condición concreta, con el artículo]

### Obligaciones que se activan
| Obligación | Norma | Responsable interno | Estado |
|---|---|---|---|

### Exposición sancionatoria
Ley 1581 art. 23: multas hasta **2.000 SMLMV**, suspensión de actividades hasta 6 meses,
cierre temporal, y **cierre inmediato y definitivo** de la operación que involucre datos
sensibles. `[verificar]`

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Datos sensibles sin justificación de necesidad es 🔴.** No basta la autorización: hay
  que poder explicar por qué se necesitan.
- **Datos de menores sin análisis de interés superior es 🔴.**
- **Condicionar un servicio a la entrega de datos sensibles es 🔴** (art. 6 par.).
- **Si no hay forma de probar la autorización, la actividad no puede proceder.** La carga
  de la prueba es del responsable.

## Lo que esta skill NO hace

- No sustituye la evaluación técnica de seguridad.
- No registra bases ante la SIC.
- No emite el concepto que solo la autoridad puede dar: si hay duda genuina, señala la
  posibilidad de consulta a la SIC.
