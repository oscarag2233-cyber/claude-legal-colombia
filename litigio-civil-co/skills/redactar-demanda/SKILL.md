---
name: redactar-demanda
description: >
  Redacta una demanda civil o comercial completa contra los requisitos del artículo 82
  del Código General del Proceso, con hechos numerados y amarrados a su prueba,
  fundamentos de derecho con citas marcadas, juramento estimatorio razonado y anexos.
  Actívela ante «redacta la demanda», «arma el escrito de demanda», «necesito demandar
  a…», «hazme la demanda de responsabilidad / de incumplimiento / de pertenencia», o
  cuando el usuario ya decidió demandar y aporta los hechos.
---

# Redactar demanda

**Antes de empezar.** Leer el perfil de práctica. Si `/litigio-civil-co:viabilidad-y-competencia`
no se ha corrido para este asunto, correrlo primero o al menos confirmar juez, cuantía,
trámite y término. Redactar sobre una competencia mal fijada desperdicia el trabajo.

*Los artículos que se citan son un mapa, no una fuente. Verificarlos contra el texto
vigente antes de radicar.*

## Lista del artículo 82 del CGP — se recorre completa

| # | Requisito | Trampa frecuente |
|---|---|---|
| 1 | Designación del juez | Poner «Juez Civil Municipal» cuando la cuantía es mayor |
| 2 | Nombre, domicilio e identificación de las partes y de sus representantes | Persona jurídica sin certificado de existencia y representación actualizado |
| 3 | Nombre y domicilio del apoderado | Falta la T.P. |
| 4 | Lo que se pretende, con precisión y claridad | Pretensiones vagas («que se condene a lo que resulte probado») |
| 5 | Hechos, debidamente determinados, clasificados y numerados | Un párrafo con quince hechos adentro |
| 6 | Fundamentos de derecho | Citas sin verificar |
| 7 | Petición de pruebas | Testigo sin dirección ni objeto de la declaración |
| 8 | Juramento estimatorio, cuando se pidan perjuicios | Cifra global sin discriminar |
| 9 | Cuantía, cuando sirva para fijar competencia o trámite | Cuantía calculada con el SMLMV del año anterior |
| 10 | Lugar y direcciones física y **electrónica** de las partes y del apoderado | Falta el correo — Ley 2213 de 2022 |

**Anexos** (art. 84): poder, prueba de existencia y representación, prueba del requisito
de procedibilidad, documentos que se tengan en poder, dictamen pericial si se aporta.

## Cómo se redactan los hechos

Esta es la parte que define si la demanda sirve.

1. **Un hecho por numeral.** Si el numeral tiene dos verbos principales, son dos hechos.
2. **Con fecha.** «En marzo» no sirve; «el 14 de marzo de 2024» sí.
3. **Con la prueba al lado, entre corchetes**, en la versión de trabajo:
   `3. El 14 de marzo de 2024 la demandada recibió la mercancía. [Remisión n.º 4521, anexo 3]`
   Los corchetes se retiran en la versión final, pero mientras se redacta obligan a ver
   qué hecho está desnudo.
4. **Solo hechos, no calificaciones.** «Actuó de mala fe» es conclusión; el hecho es lo
   que hizo. La calificación va en los fundamentos de derecho.
5. **Orden cronológico**, salvo que la estructura del caso pida otra cosa.
6. **Todo hecho de la pretensión debe estar en los hechos.** Y todo hecho debe servir
   para algo: si un numeral no sostiene ninguna pretensión ni desactiva una defensa
   previsible, sobra.

**Al terminar los hechos, correr esta comprobación cruzada:**

| Elemento de la pretensión | Hecho que lo afirma | Prueba |
|---|---|---|
| [existencia del contrato] | Hecho 2 | Anexo 1 |
| [incumplimiento] | Hechos 5, 6 | Anexos 4, 5 |
| [daño] | Hecho 8 | Dictamen |

Cualquier casilla vacía es un 🔴 antes de radicar.

## Pretensiones

- **Principales**, **subsidiarias** (se piden «en subsidio de») y **accesorias**
  (intereses, corrección monetaria, costas).
- Redactar como orden al juez: «DECLARAR que…», «CONDENAR a… a pagar…».
- **Consecuenciales bien atadas:** si se pide resolución del contrato, pedir también la
  restitución de lo pagado; si se pide nulidad, pedir las restituciones mutuas.
- **Costas y agencias en derecho** siempre.
- **Intereses:** decir cuáles (moratorios comerciales del art. 884 C.Co., o los del
  art. 1617 CC), desde cuándo y hasta cuándo.

## Fundamentos de derecho

- **Norma sustancial primero**, procesal después.
- **Una regla por párrafo**, con la norma y, si aplica, la jurisprudencia que la
  interpreta — extrayendo la *ratio* en una frase, no transcribiendo tres páginas.
- **Toda cita se etiqueta** conforme a los guardarraíles del perfil. Antes de radicar,
  correr `/litigio-civil-co:verificar-citas`.

## Juramento estimatorio (CGP art. 206)

Obligatorio cuando se pidan perjuicios, frutos, mejoras o cosas semejantes.

- **Razonado y discriminado**: rubro por rubro, con la base de cálculo.
- **No inflar.** El art. 206 prevé sanción cuando la estimación excede en más del 50% a
  lo probado. La Corte Constitucional condicionó su aplicación en la Sentencia
  **C-157 de 2013**: exige negligencia o temeridad, no basta la diferencia `[verificar]`.
  Pero la sanción del inciso sobre pretensiones negadas por falta de prueba del
  perjuicio sigue siendo un riesgo real.
- Fórmula usable:

```
Estimo bajo juramento la cuantía de los perjuicios en $[X], discriminada así:
  a) Daño emergente: $[…] — [base: facturas anexos 6 a 9]
  b) Lucro cesante consolidado: $[…] — [base: fórmula, período, renta]
  c) Lucro cesante futuro: $[…] — [base]
  d) Perjuicio moral: [N] SMLMV — [base: parentesco / prueba]
Esta estimación se hace con fundamento en [documentos/dictamen] y sin perjuicio de lo
que resulte probado en el proceso.
```

Ver `referencias/cuantificacion-de-perjuicios.md`.

## Pruebas

Por cada medio:

- **Documental:** lista numerada, con lo que prueba cada documento. Recordar la
  presunción de autenticidad del art. 244.
- **Testimonial:** nombre, dirección **y objeto de la declaración** — «declarará sobre
  los hechos 4 a 7». Sin objeto, el juez puede rechazarla.
- **Pericial:** el dictamen de parte se **aporta con la demanda** (art. 227). Si no se
  tiene, pedirlo y explicar por qué no se pudo aportar.
- **Interrogatorio de parte** al demandado.
- **Exhibición** de documentos que estén en poder del demandado o de un tercero.
- **Oficios** a entidades, con lo que se pide a cada una.
- **Inspección judicial**, cuando el objeto material importe.

## Medidas cautelares

Si se van a pedir, va sección aparte y se remite a
`/litigio-civil-co:medidas-cautelares`. Recordar que pedir cautelares suele exceptuar
del requisito de conciliación previa `[verificar]`.

## Salida

Documento completo listo para revisión, con esta estructura:

```
Señor(a)
JUEZ [ ] CIVIL [MUNICIPAL/DEL CIRCUITO] DE [CIUDAD] (REPARTO)
E. S. D.

Referencia: PROCESO [VERBAL / VERBAL SUMARIO / EJECUTIVO]
Demandante: [ ]
Demandado: [ ]

[Nombre], mayor de edad, identificado con C.C. n.º [ ], abogado en ejercicio con
T.P. n.º [ ] del C. S. de la J., actuando como apoderado de [ ], según poder que
adjunto, me permito presentar demanda [ ] contra [ ], con fundamento en los
siguientes:

I. PRETENSIONES
II. HECHOS
III. FUNDAMENTOS DE DERECHO
IV. JURAMENTO ESTIMATORIO
V. PRUEBAS
VI. MEDIDAS CAUTELARES  [si aplica]
VII. COMPETENCIA Y CUANTÍA
VIII. ANEXOS
IX. NOTIFICACIONES
```

**Después del documento, siempre:**

```markdown
### Campos pendientes antes de radicar
[lista explícita de todo lo que quedó entre corchetes o sin dato]

### Verificación de citas
[N] citas normativas y [N] jurisprudenciales. Corra `/litigio-civil-co:verificar-citas`
antes de radicar.

### Comprobación cruzada hechos ↔ pretensiones ↔ prueba
[la tabla, con los vacíos marcados]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Nunca entregar una demanda con `[ ]` sin listar explícitamente qué falta.**
- **No radicar sin verificar citas.** Decirlo en el cierre, siempre.
- **Si el Rol no es abogado inscrito:** la demanda no se radica sin abogado. La
  compuerta del perfil aplica en pleno.

## Lo que esta skill NO hace

- No radica ni firma.
- No fija la cuantía por el usuario si los soportes no la respaldan: la calcula y marca
  lo que no está probado.
- No garantiza admisión: reduce las causales de inadmisión del art. 90, que son las que
  se pueden controlar desde el escritorio.
