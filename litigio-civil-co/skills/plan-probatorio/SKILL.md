---
name: plan-probatorio
description: >
  Convierte la teoría del caso en un plan de prueba operativo: qué hecho hay que probar,
  con qué medio, quién lo tiene, cómo se pide y en qué oportunidad procesal. Actívela
  ante «¿con qué pruebo esto?», «arma el plan probatorio», «qué pruebas pido», «cómo
  demuestro que…», «necesito un dictamen», o cuando el usuario tenga los hechos claros y
  no sepa cómo acreditarlos.
---

# Plan probatorio

**Antes de empezar.** Leer el perfil y, si hay asunto activo, su contexto. Esta skill
funciona mejor después de `/litigio-civil-co:viabilidad-y-competencia` y antes de
`/litigio-civil-co:redactar-demanda` o `/litigio-civil-co:contestar-demanda`.

*Los artículos citados son un mapa. Verificarlos antes de usarlos.*

## Punto de partida: la matriz

Todo el plan es una tabla. Se construye de izquierda a derecha y no se avanza sin
llenar la columna anterior.

| Elemento jurídico | Hecho que hay que probar | Medio | Quién lo tiene | Cómo se pide | Oportunidad | Estado |
|---|---|---|---|---|---|---|
| Existencia del contrato | Se celebró el 3-02-2024 | Documental | Cliente | Se aporta | Con la demanda | ✅ |
| Incumplimiento | No entregó el 30-04 | Documental + testimonial | Cliente y tercero | Aportar + testimonio | Con la demanda | ⚠️ falta dirección del testigo |
| Daño | Pérdida de $X | Pericial | Perito de parte | Dictamen aportado | Con la demanda (art. 227) | 🔴 no se ha contratado |
| Nexo causal | | | | | | |

**Regla:** ningún elemento jurídico puede quedar con la fila vacía. Un elemento sin
prueba es una pretensión que se va a negar.

## Carga de la prueba (CGP art. 167)

- **Regla general:** incumbe a la parte probar el supuesto de hecho de las normas que
  consagran el efecto jurídico que persigue.
- **Carga dinámica:** el juez puede, de oficio o a petición, distribuir la carga
  exigiendo probar a la parte que esté en mejor posición de hacerlo — por cercanía al
  material probatorio, por tener el objeto, por circunstancias técnicas, por su estado
  de indefensión o por su condición profesional. **Si el caso lo permite, pedirla
  expresamente y sustentarla**: es una de las herramientas más desaprovechadas del CGP.
- **Presunciones:** identificar si alguna opera a favor. Quien tiene presunción a favor
  prueba el hecho base, no el presumido.
- **Hechos que no requieren prueba:** los admitidos, los notorios, las afirmaciones o
  negaciones indefinidas (art. 167 inc. final).

## Medios de prueba y sus reglas prácticas

### Documental (arts. 243-252)

- **Presunción de autenticidad** de los documentos (art. 244): los documentos son
  auténticos mientras no se tachen de falsos. Esto cambió mucho la práctica: ya no hay
  que autenticar todo.
- **Documento en poder de la contraparte o de tercero:** pedir **exhibición** (arts.
  265-268). Si se niega sin justificación, hay consecuencias probatorias.
- **Mensajes de datos y WhatsApp:** son documentos (Ley 527 de 1999). Aportarlos con la
  cadena completa, no con capturas sueltas, y decir cómo se obtuvieron.
- Numerar los anexos y decir **qué prueba cada uno**. Un anexo sin explicación es un
  anexo que el juez no va a leer.

### Testimonial (arts. 208-225)

- En la petición: **nombre, dirección y objeto de la declaración**. Sin objeto, se
  rechaza.
- **Escoger pocos y buenos.** Cinco testigos que dicen lo mismo pesan menos que dos que
  vieron cosas distintas.
- **Testigo técnico** frente a **perito**: el testigo declara sobre lo que percibió,
  aunque tenga conocimiento especializado; el perito emite opinión. No confundirlos.
- **Tacha** (art. 211): las circunstancias que afecten la credibilidad se alegan y se
  prueban; no descalifican automáticamente.

### Pericial (arts. 226-235)

**Este es el cambio de mentalidad más importante del CGP:** el dictamen es de parte y
**se aporta con la demanda o con la contestación** (art. 227). No se «pide un perito»
como antes.

- Requisitos del dictamen (art. 226): identificación del perito, su idoneidad,
  documentos que la acrediten, método, fundamentos, declaración sobre su independencia.
- La contraparte puede pedir la **comparecencia del perito** a la audiencia para
  interrogarlo, o aportar **contradictamen**.
- **Si no se tiene dictamen y se necesita**, decirlo con tiempo: conseguir perito toma
  semanas y cuesta. Un plan probatorio que descubre a última hora que hace falta un
  dictamen ya falló.

### Interrogatorio de parte (arts. 198-205)

- **Confesión** (art. 191): la de la parte tiene valor propio. Pensar el interrogatorio
  para obtener confesión sobre hechos concretos, no para discutir.
- **Inasistencia injustificada:** consecuencias del art. 205 — se presumen ciertos los
  hechos susceptibles de confesión de la demanda o de las excepciones.

### Inspección judicial (arts. 236-238)

Procede cuando el juez debe percibir directamente. Es costosa en tiempo; pedirla solo
cuando el objeto material sea decisivo, y **con el cuestionario listo**.

### Indicios (arts. 240-242)

No son un medio autónomo que se «pida»: se construyen en los alegatos a partir de
hechos probados. Si el caso se va a ganar por indicios, **decirlo desde el plan** para
asegurar la prueba de los hechos indicadores.

### Prueba trasladada (art. 174)

Se puede traer prueba de otro proceso si se practicó con audiencia de la parte contra
quien se aduce, o si se ratifica. Verificarlo antes de confiar en ella.

## Oportunidades procesales — no se pierden dos veces

| Momento | Qué se puede hacer |
|---|---|
| Demanda / contestación | Aportar documentos y dictámenes; pedir todas las pruebas |
| Reforma de la demanda (art. 93) | Ajustar la petición de pruebas |
| Audiencia inicial (art. 372) | Fijación del litigio, decreto de pruebas, interrogatorios |
| Audiencia de instrucción y juzgamiento (art. 373) | Práctica, alegatos, sentencia |
| Segunda instancia (art. 327) | Pruebas solo en los casos taxativos |

**La fijación del litigio en la audiencia inicial define qué se prueba.** Llegar a esa
audiencia sin la lista de hechos que se van a fijar es entregar el control del proceso.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Plan probatorio — [asunto]

### Teoría del caso en una frase
[qué queremos que el juez concluya y por qué]

### Matriz
[la tabla completa]

### 🔴 Vacíos que hay que cerrar antes de radicar
| Elemento | Qué falta | Quién lo consigue | Para cuándo |
|---|---|---|---|

### Carga de la prueba
- Lo que nos toca probar: […]
- Lo que le toca a la contraparte: […]
- ¿Pedimos carga dinámica? [sí, sobre X, porque…] / [no]
- Presunciones a favor: […]

### Petición de pruebas, redactada
[texto listo para insertar en la demanda o contestación]

### Costos y tiempos estimados
| Prueba | Costo | Tiempo de consecución |
|---|---|---|

### Riesgos probatorios
[qué pasa si el testigo no llega, si el dictamen se objeta, si no exhiben]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Todo elemento jurídico sin prueba es 🔴 y va al principio.**
- **Si el caso necesita dictamen pericial y no hay perito**, decirlo con el tiempo de
  consecución estimado. Es la falla más frecuente y la menos recuperable.
- **No proponer prueba ilícita ni obtenida con violación del debido proceso**
  (Const. art. 29): es nula de pleno derecho y contamina.

## Lo que esta skill NO hace

- No consigue las pruebas.
- No entrevista testigos ni prepara declaraciones — preparar a un testigo para que
  declare distinto de lo que percibió es inducción a falso testimonio.
- No sustituye el criterio del abogado sobre qué batalla dar.
