---
name: ia-en-la-practica-juridica
description: >
  Reglas de uso de IA en piezas que se radican o se entregan a clientes: verificación
  obligatoria de citas, transparencia frente al despacho y al cliente, reserva profesional
  y deberes del Estatuto del Abogado. Actívela ante «puedo usar IA para un memorial»,
  «hay que decirle al juez que usé IA», «citas inventadas», «responsabilidad del abogado
  que usa IA», «protocolo de uso de IA en el despacho», «IA en la Rama Judicial».
---

# IA en la práctica jurídica

**Antes de empezar.** Leer el perfil. Esta skill es la que traduce toda la gobernanza de
IA al oficio concreto de litigar y asesorar en Colombia.

> **El riesgo número uno del uso de IA en Derecho no es la confidencialidad: es la cita
> que parece correcta y no existe.** Todo lo demás de esta skill se ordena alrededor de
> ese problema.

## Regla 1 — Verificación de citas: no negociable

**Ninguna pieza sale del despacho con una cita que no se haya verificado en fuente
oficial.**

| Elemento | Verificación mínima |
|---|---|
| **Norma** | Que exista, que el artículo diga lo que se afirma, que esté vigente, que no tenga inexequibilidad ni condicionamiento |
| **Sentencia** | Que exista con esa nomenclatura, que sea de esa corporación, que lo citado sea *ratio* y no *obiter*, que la línea no haya cambiado |
| **Concepto de autoridad** | Número, fecha, vigencia |
| **Término** | Norma que lo fija, tipo de días, día de inicio |
| **Cifra** | Año de la UVT o del SMLMV, tarifa vigente |

**Herramienta:** `/gobernanza-ia-co:verificar-citas` en este plugin, y la skill homónima
en cada plugin del marketplace. Ver también
`referencias/verificacion-de-fuentes.md`.

**Por qué es no negociable:** presentar autoridad inexistente o tergiversada puede
configurar falta a los deberes de **diligencia** y **lealtad** del abogado (Ley 1123 de
2007, arts. 33 y 34), además de exponer a las consecuencias procesales de la temeridad y
la mala fe (CGP arts. 78 y 79). Y en varios países ya ha producido sanciones concretas a
abogados. El riesgo no es teórico.

**La regla de oro:** *si no la recuperó de la relatoría o de SUIN-Juriscol en esta sesión,
no está verificada, por segura que suene.*

## Regla 2 — Reserva profesional

| Regla | Fundamento |
|---|---|
| **La información del cliente no entra a herramientas sin contrato de tratamiento.** | Const. art. 74; Ley 1123 de 2007, art. 34 lit. f; Ley 1581 de 2012 |
| **Anonimizar antes de procesar**, siempre que sea posible | `referencias/tratamiento-de-datos.md` |
| **Las herramientas gratuitas o personales no sirven para expedientes.** | Sus términos suelen incluir entrenamiento con el contenido |
| **Verificar dónde se almacena y quién puede acceder** | → `/gobernanza-ia-co:revision-de-proveedor-ia` |
| **La reserva sobrevive a la terminación del encargo** | |

**La reserva profesional es más exigente que la ley de datos:** rige aunque el titular
consienta, porque protege también la confianza en la profesión.

## Regla 3 — Transparencia: a quién se le dice qué

| Frente al… | ¿Se informa? |
|---|---|
| **Cliente** | **Sí**, cuando el uso de IA sea relevante para el encargo, para la confidencialidad o para los honorarios. El deber de información veraz del art. 33 de la Ley 1123 lo respalda. Y si va a procesar información suya en una herramienta de terceros, **pedir autorización informada** |
| **Despacho judicial** | **Si el despacho lo exige, sí, sin excepción.** Varios despachos ya lo requieren. Fuera de eso, la práctica está en construcción: la regla segura es informarlo cuando la herramienta incidió de forma relevante en la elaboración de la pieza `[verificar los lineamientos vigentes del Consejo Superior de la Judicatura]` |
| **Contraparte** | No hay deber general |
| **Autoridad administrativa** | Según lo que exija cada trámite |

**Lo que nunca es aceptable:** afirmar que una cita fue verificada cuando no lo fue, o
sostener ante el juez que un error de citación fue del asistente. **La responsabilidad es
de quien firma.**

## Regla 4 — La IA no ejerce la abogacía

| Lo que la IA puede hacer | Lo que no puede hacer |
|---|---|
| Preparar borradores | Firmar |
| Organizar hechos y cronologías | Otorgar o recibir poder |
| Sugerir estructuras y argumentos | Comparecer |
| Buscar y proponer fuentes **para verificar** | Emitir concepto jurídico |
| Revisar documentos y marcar hallazgos | Decidir la estrategia |
| Calcular términos **para verificar** | Asumir responsabilidad profesional |
| Traducir a lenguaje claro | Sustituir el juicio del abogado |

**Fundamento:** el ejercicio de la abogacía está reservado a quien tiene tarjeta
profesional vigente (Decreto 196 de 1971; Ley 1123 de 2007). Ver
[`AVISO-LEGAL.md`](../../../AVISO-LEGAL.md).

## Regla 5 — Uso en actuaciones judiciales

| Marco | Contenido |
|---|---|
| **Ley 2213 de 2022** | Uso permanente de TIC en actuaciones judiciales; memoriales y notificaciones electrónicas; presunción de autenticidad de los mensajes remitidos desde las direcciones inscritas |
| **Lineamientos del Consejo Superior de la Judicatura sobre IA en la Rama Judicial** | `[verificar acuerdo o circular vigente]` |
| **Jurisprudencia constitucional sobre uso de IA en providencias judiciales** | La Corte se ha pronunciado sobre el uso de IA generativa por jueces, en clave de debido proceso, juez natural, motivación y transparencia. **Verificar la sentencia y su alcance antes de citarla** `[conocimiento del modelo — verificar]` |
| **Deber de lealtad procesal** | CGP arts. 78 y 79 |

## Protocolo del despacho — para adoptar

```markdown
PROTOCOLO DE USO DE IA — [Firma / Departamento jurídico]

1. HERRAMIENTAS AUTORIZADAS
   [Lista, con contrato de tratamiento vigente]

2. INFORMACIÓN QUE NO ENTRA
   - Expedientes y documentos de clientes en herramientas no autorizadas
   - Datos personales sin anonimizar
   - Estrategia procesal
   - Credenciales

3. VERIFICACIÓN OBLIGATORIA
   Toda norma, sentencia, término y cifra se verifica en fuente oficial antes de
   radicar o entregar. Se deja constancia en la bitácora de verificación.

4. FIRMA Y RESPONSABILIDAD
   La pieza la revisa y la firma un abogado con tarjeta profesional vigente, que asume
   la responsabilidad profesional.

5. TRANSPARENCIA
   - Con el cliente: [regla de la casa]
   - Con el despacho: se informa cuando el despacho lo exija o cuando la herramienta
     haya incidido de forma relevante

6. REGISTRO
   Bitácora de verificación por asunto; registro de herramientas usadas.

7. CAPACITACIÓN
   [Periodicidad] con casos reales de la firma.

8. INCUMPLIMIENTO
   [Consecuencias]
```

## Lista de chequeo antes de radicar

```
[ ] ¿Todas las normas citadas fueron verificadas en fuente oficial?
[ ] ¿Todas las sentencias existen y lo citado es la ratio?
[ ] ¿Se verificó la vigencia y los condicionamientos?
[ ] ¿Los términos se calcularon con la norma y contra el calendario judicial?
[ ] ¿Las cifras corresponden al año aplicable?
[ ] ¿Se anonimizó lo que debía anonimizarse?
[ ] ¿No entró información de cliente a herramientas no autorizadas?
[ ] ¿Un abogado con T.P. vigente revisó la pieza completa?
[ ] ¿Quedan marcas `[verificar]` sin resolver?
[ ] ¿El despacho exige informar el uso de IA? ¿Se informó?
```

**Si alguna casilla queda sin marcar, la pieza no se radica.**

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Uso de IA — [asunto o consulta]

### Situación
[qué se quiere hacer con IA]

### Análisis
| Regla | Aplicación al caso | Semáforo |
|---|---|---|
| Verificación de citas | | |
| Reserva profesional | | |
| Transparencia | | |
| Reserva de la abogacía | | |
| Actuaciones judiciales | | |

### 🔴 Condiciones
1. [ ]

### Lista de chequeo antes de radicar
[la lista, aplicada al caso]

---
[PROTOCOLO / COMUNICACIÓN AL CLIENTE / NOTA AL DESPACHO, si se pidieron]
---

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **La verificación de citas no es negociable.** Ninguna salida de esta skill relativiza
  esa regla.
- **Información de cliente en herramienta no autorizada es 🔴.**
- **No sugerir que se oculte el uso de IA cuando el despacho lo exige.**
- **No presentar una salida de IA como concepto jurídico.**
- **Si el usuario no es abogado inscrito**, la compuerta de revisión profesional del perfil
  aplica en pleno.

## Lo que esta skill NO hace

- No verifica las citas por sí sola: para eso está `/gobernanza-ia-co:verificar-citas`.
- No sustituye los lineamientos del despacho ni de la Rama Judicial: remite a ellos.
- No exime de responsabilidad profesional a nadie.
