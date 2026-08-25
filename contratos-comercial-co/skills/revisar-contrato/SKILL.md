---
name: revisar-contrato
description: >
  Revisa un contrato civil o mercantil cláusula por cláusula contra los criterios de la
  casa y contra el derecho imperativo colombiano, marca desviaciones con severidad dual
  y propone redlines quirúrgicos. Actívela ante «revisa este contrato», «me mandaron
  este contrato», «¿puedo firmar esto?», «qué le cambio a este contrato», «revisión de
  clausulado», o cuando el usuario adjunte un contrato.
---

# Revisar contrato

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/contratos-comercial-co/CLAUDE.md`.
Si `## Criterios de la casa` está en `[PENDIENTE]`, detenerse: sin posiciones de la casa
la revisión es una opinión genérica. Remitir a `/contratos-comercial-co:entrevista-inicial`.

## Paso 0 — De qué lado estamos

Antes de aplicar cualquier criterio: **¿quién es nuestro cliente en este contrato?**
Proveedor o cliente, arrendador o arrendatario, mandante o mandatario, franquiciante o
franquiciado. Un tope de responsabilidad que protege a uno perjudica al otro. Si no es
obvio, preguntar. **Registrar en la salida de qué lado se revisó.**

## Paso 1 — Calificación del contrato

Antes de leer las cláusulas hay que saber qué contrato es. La calificación cambia el
régimen supletivo y las normas imperativas que aplican.

| Pregunta | Por qué importa |
|---|---|
| ¿Es civil o mercantil? | C.Co. art. 1 y 20-22. Si al menos una parte es comerciante y el acto es mercantil, aplica el Código de Comercio; el Civil se aplica supletivamente (C.Co. art. 822) |
| ¿Hay un consumidor? | Si sí, aplica la **Ley 1480 de 2011** con normas imperativas y control de cláusulas abusivas. Remitir a `/consumidor-competencia-co:publicidad-y-clausulas-abusivas` |
| ¿Qué tipo contractual es realmente? | El nombre no manda. Un «contrato de prestación de servicios» que es agencia comercial genera cesantía comercial (C.Co. art. 1324) |
| ¿Es de adhesión? | Se interpreta contra quien lo redactó (C.Co. art. 1624 CC: cláusulas ambiguas contra quien las dictó) |
| ¿Hay elemento internacional? | Ley aplicable, arbitraje internacional (Ley 1563 de 2012), CISG si aplica |

**Tipos que esconden otro tipo — verificar siempre:**
- Distribución / suministro que en realidad es **agencia comercial** → cesantía comercial
  e indemnización equitativa (C.Co. arts. 1317-1331). Es la contingencia comercial más
  cara y más ignorada en Colombia.
- Prestación de servicios que es **contrato de trabajo** → remitir a
  `/laboral-seguridad-social-co:vinculacion-y-tercerizacion`.
- Compraventa con pacto de reserva de dominio, leasing, fiducia: cada uno con su régimen.

## Paso 2 — Derecho imperativo: lo que ninguna cláusula puede

Este barrido va antes que los criterios de la casa, porque **el cliente puede fijar su
política pero no puede pactar lo que la ley prohíbe**:

| Regla | Norma | Efecto |
|---|---|---|
| No se condona el dolo futuro | CC art. 1522 | Objeto ilícito → nulidad absoluta |
| La culpa grave equivale al dolo | CC art. 63 | No se puede exonerar de ella |
| La cláusula penal no excede el duplo de la obligación principal (obligaciones de cantidad determinada) | CC art. 1601 | Reducible por el juez |
| La pena se reduce en proporción al cumplimiento parcial | CC art. 1596 | |
| Intereses: tope de usura | C.Co. art. 884; CP art. 305 | Pérdida de intereses y exposición penal |
| Buena fe en la celebración y ejecución | CC art. 1603; C.Co. art. 871 | Fuente de obligaciones no escritas |
| Abuso del derecho | C.Co. art. 830 | Genera indemnización |
| Lesión enorme en compraventa de inmuebles | CC arts. 1946-1954 | Rescisión, 4 años |
| Objeto y causa lícitos | CC arts. 1519-1524 | Nulidad absoluta |
| Cláusulas abusivas si hay consumidor | Ley 1480 arts. 42-43 | Ineficacia de pleno derecho |
| Prohibición de pactar renuncia previa a la cesantía comercial (agencia) | C.Co. art. 1324 y jurisprudencia `[verificar]` | |

## Paso 3 — Recorrido de cláusulas

Se recorren todas, con esta rejilla por cada una:

```
[N.º y nombre de la cláusula]
  Qué dice: [una línea]
  Posición de la casa: [la del perfil, o «el perfil no la cubre»]
  Desviación: [ninguna / cuál]
  Riesgo jurídico: 🔴/🟠/🟡/🟢   Fricción de negocio: 🔴 bloquea / 🟠 demora / 🟡 confunde / 🟢 invisible
  Redline propuesto: [el mínimo cambio que logra la posición]
```

**Cláusulas que siempre se revisan aunque el perfil no las nombre:**

1. **Objeto y alcance** — ¿está delimitado o es abierto?
2. **Precio, forma de pago, reajuste** — IPC, fórmula, moneda. Si es en moneda
   extranjera, revisar régimen cambiario.
3. **Plazo, prórroga y terminación** — automática o con preaviso; terminación unilateral
   y su indemnización.
4. **Obligaciones de cada parte** — asimetrías.
5. **Responsabilidad y límites** — ver Paso 2.
6. **Cláusula penal** — tope, si es compensatoria o moratoria, si se acumula con
   perjuicios (CC art. 1594: no se acumula salvo pacto expreso).
7. **Garantías** — pólizas, aval, prenda, hipoteca, fiducia. Vigencia y amparos.
8. **Confidencialidad** — duración, excepciones, destino de la información.
9. **Propiedad intelectual** — quién es titular de lo desarrollado; **en Colombia los
   derechos morales son inalienables** (Ley 23 de 1982). Remitir a
   `/propiedad-intelectual-co:contratos-de-pi`.
10. **Protección de datos** — si hay tratamiento por cuenta ajena, se necesita cláusula
    o contrato de transmisión (Decreto 1074 de 2015, art. 2.2.2.25.5.2) `[verificar]`.
    Remitir a `/datos-personales-co:contrato-de-encargo` `[si existe]`.
11. **Cesión y subcontratación.**
12. **Fuerza mayor** — definición, efectos, deber de mitigar (CC art. 64, mod. Ley 95 de
    1890).
13. **Ley aplicable y solución de controversias** — jurisdicción ordinaria o arbitraje;
    si arbitraje: centro, número de árbitros, en derecho o en equidad, sede, idioma.
    **Un pacto arbitral mal redactado es una cláusula patológica que cuesta un año.**
14. **Notificaciones** — direcciones físicas y **electrónicas**, con efectos.
15. **Integridad, modificaciones y anexos** — orden de prelación entre documentos.

## Paso 4 — Redlines quirúrgicos

**Edite en la menor granularidad posible.** Un redline es un artefacto de negociación,
no una reescritura:

- Cambiar una **palabra** antes que una frase. («doce (12)» → «veinticuatro (24)»)
- Cambiar una **frase** antes que una oración.
- Reestructurar un **literal** antes que reemplazar la oración.
- Reemplazar una **cláusula entera** solo cuando la versión de la contraparte esté tan
  lejos de la posición que los cambios quirúrgicos serían más difíciles de leer. Y
  cuando se haga, decirlo en la carta remisoria.

Quien recibe un redline quirúrgico entiende que se leyó con cuidado. Quien recibe una
cláusula reemplazada entera se pregunta si se leyó.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Revisión — [contrato] — [contraparte]

**Revisado del lado de:** [nuestro cliente como ___]
**Tipo contractual:** [calificación real, si difiere del nombre] — [régimen aplicable]

### Resumen ejecutivo
- [Edición accionable en una línea]
- [Edición accionable en una línea]
- [Máximo cinco. Solo acciones mecánicas: suprimir, cambiar, agregar]

### 🔴 Bloqueantes
| # | Cláusula | Problema | Norma | Redline |
|---|---|---|---|---|

### 🟠 y 🟡 — para decisión
| # | Cláusula | Desviación de la posición | Riesgo jurídico | Fricción | Redline |
|---|---|---|---|---|---|

### Riesgos que no están en el texto — lo que falta
| Falta | Por qué importa | Cláusula sugerida |
|---|---|---|

### Recorrido completo
[la rejilla, cláusula por cláusula]

### Posiciones que el perfil no cubre
[cada una, con la pregunta que hay que hacerle al cliente para incorporarla al perfil]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

**Filtro de complejidad:** si atender un problema exige redactar cláusula nueva,
reestructurar o insertar régimen sustantivo nuevo, **no lo intente en el resumen
ejecutivo**. Escriba «Cláusula [X] — remitir a revisión de abogado». El resumen
ejecutivo solo lleva acciones mecánicas.

**Contrato limpio:** si pasa todas las verificaciones, el resumen ejecutivo dice
solamente: «Sin desviaciones frente a las posiciones de la casa. Puede firmarse por el
trámite estándar.» No producir un informe largo para un contrato limpio.

## Compuertas

- **Todo hallazgo de derecho imperativo es 🔴**, aunque el criterio de la casa lo permita.
- **Si aparece agencia comercial encubierta, es 🔴** y va primero.
- **Si el Rol no es abogado inscrito**, firmar no pasa sin la compuerta de revisión
  profesional.
- **Verificación de destinatario** antes de mandar la revisión a la contraparte.

## Lo que esta skill NO hace

- No negocia.
- No fija posiciones: las lee del perfil y pregunta lo que falta.
- No firma ni autoriza.
