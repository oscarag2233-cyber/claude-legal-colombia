---
name: tipo-societario-y-constitucion
description: >
  Escoge el tipo societario por las razones correctas y arma el documento de constitución
  con los estatutos que el negocio necesita, incluida la SAS por documento privado.
  Actívela ante «voy a crear una empresa», «SAS o SA», «qué tipo de sociedad me
  conviene», «constituir sociedad», «estatutos», «sucursal de sociedad extranjera», o
  cuando alguien vaya a formalizar un negocio.
---

# Tipo societario y constitución

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/societario-co/CLAUDE.md`.

## Paso 1 — Las preguntas que definen el tipo

No se escoge el tipo por costumbre. Se escoge por las respuestas a estas seis preguntas:

1. **¿Cuántos socios y quiénes son?** ¿Habrá inversionistas después?
2. **¿Hace falta limitar la responsabilidad?** Casi siempre sí.
3. **¿Cómo va a entrar y salir gente?** ¿Se quiere controlar quién entra?
4. **¿Habrá derechos económicos o políticos diferenciados?** (acciones con voto múltiple,
   con dividendo preferencial, de pago)
5. **¿Se prevé inversión extranjera, ronda de capital o venta futura?**
6. **¿Hay actividad vigilada?** (financiera, aseguradora, vigilancia privada, salud,
   servicios públicos) — puede imponer el tipo y el capital mínimo.

## Paso 2 — Comparación

| | **SAS** (Ley 1258 de 2008) | **SRL** | **SA** | **Sucursal de sociedad extranjera** |
|---|---|---|---|---|
| Constitución | **Documento privado** inscrito en registro mercantil (art. 5) — escritura pública solo si se aportan inmuebles | Escritura pública | Escritura pública | Escritura pública, con documentos de la casa matriz |
| Socios | 1 o más | 2 a 25 | Mínimo 5 accionistas | No aplica |
| Responsabilidad | Limitada al aporte, **incluso por obligaciones laborales y tributarias** (art. 1), salvo desestimación | Limitada, **con excepciones laborales y tributarias** | Limitada al aporte | La matriz responde |
| Objeto | **Indeterminado** permitido | Determinado | Determinado | El de la matriz |
| Duración | **Indefinida** permitida | Determinada | Determinada | |
| Junta directiva | Opcional | Opcional | **Obligatoria** (mínimo 3 principales con suplentes) | |
| Revisor fiscal | Solo si supera los topes legales `[verificar]` | Según topes | **Obligatorio** | Según el caso |
| Acciones | Ordinarias, privilegiadas, con dividendo preferencial y sin voto, **de pago** | Cuotas — cesión requiere reforma estatutaria | Ordinarias y privilegiadas | |
| Negociabilidad | Libre, salvo restricción estatutaria (derecho de preferencia, autorización previa) | **Derecho de preferencia legal** y reforma estatutaria para ceder | Libre | |
| Conflictos | **Superintendencia de Sociedades** en función jurisdiccional (art. 40) o arbitraje | Juez o Supersociedades | | |
| Flexibilidad estatutaria | **Muy alta** | Baja | Media | |

**En la práctica colombiana, la SAS es la respuesta por defecto** y con buena razón:
constitución por documento privado, un solo accionista, objeto indeterminado, duración
indefinida, libertad estatutaria y foro especializado.

**Cuándo NO es la respuesta:** actividades que exigen otro tipo por ley; sociedades que
van a emitir en el mercado público de valores; estructuras que requieren junta directiva
con régimen legal estricto por exigencia de un inversionista o de un financiador.

## Paso 3 — Lo que hay que decidir antes de redactar estatutos

Estas son las decisiones que después cuestan caro cambiar:

| Decisión | Opciones | Consecuencia |
|---|---|---|
| **Objeto** | Indeterminado / determinado | El indeterminado da flexibilidad; algunos bancos y contratantes exigen determinado |
| **Capital** | Autorizado, suscrito y pagado | En SAS el pago puede diferirse hasta **2 años** (Ley 1258 art. 9) |
| **Clases de acciones** | Ordinarias, privilegiadas, con dividendo preferencial sin voto, de pago | Definir desde el inicio evita reformas |
| **Restricción a la negociación** | Derecho de preferencia, autorización previa de la asamblea, **restricción por hasta 10 años** (art. 13) | Es lo que impide que entre alguien no deseado |
| **Órganos** | Asamblea + representante legal / + junta directiva | En SAS la junta es opcional |
| **Facultades del representante legal** | Amplias / limitadas por cuantía o materia | **Las limitaciones inscritas son oponibles a terceros** |
| **Quórum y mayorías** | Legales o estatutarias | Se puede pactar unanimidad para ciertas materias |
| **Reuniones no presenciales y voto por escrito** | Habilitarlas expresamente | Ley 222 arts. 19-21, mod. Ley 2069 de 2020 |
| **Solución de controversias** | Supersociedades / arbitraje | La Supersociedades es especializada y más barata |
| **Cláusulas de salida** | Arrastre, acompañamiento, opción de compra, valoración | Sin ellas, salir de una SAS puede ser imposible |

**Advertencia sobre responsabilidad:** el art. 1 de la Ley 1258 limita la
responsabilidad del accionista de SAS incluso frente a obligaciones laborales y
tributarias, **pero** el art. 42 permite la **desestimación de la personalidad jurídica**
cuando la SAS se usa en fraude a la ley o en perjuicio de terceros, y el art. 43 sanciona
el **abuso del derecho de voto**. Además, los administradores responden por sus propias
faltas. La limitación protege al accionista diligente, no al que instrumentaliza la
sociedad.

## Paso 4 — El documento de constitución (Ley 1258, art. 5)

Contenido mínimo:

1. Nombre, documento de identidad y domicilio de los accionistas.
2. **Razón social o denominación seguida de «SAS»** o «Sociedad por Acciones
   Simplificada». Verificar homonimia en el RUES antes.
3. **Domicilio principal** y de las sucursales.
4. **Término de duración** (puede ser indefinido).
5. **Objeto social** (puede ser indeterminado).
6. **Capital autorizado, suscrito y pagado**, clase, número y valor nominal de las
   acciones, y forma y términos de pago.
7. **Forma de administración**, con documento de identidad y facultades de los
   administradores; al menos un **representante legal**.

Si se aportan inmuebles, **escritura pública** (art. 5 par. 2).

## Paso 5 — Trámites posteriores a la constitución

| Trámite | Ante quién | Nota |
|---|---|---|
| Inscripción en registro mercantil | Cámara de comercio | Da existencia a la sociedad |
| **RUT y NIT** | DIAN | Suele hacerse en la misma ventanilla |
| Libros: registro de accionistas, actas de asamblea | Cámara de comercio | El **libro de registro de accionistas** es lo que prueba la calidad de accionista |
| Registro de la inversión extranjera | Banco de la República | Si hay capital del exterior. **Plazo y formulario propios** `[verificar]` |
| Facturación electrónica y responsabilidades tributarias | DIAN | |
| Afiliaciones al sistema de seguridad social | | Si hay trabajadores |
| Registro de marca | SIC | Ver `/propiedad-intelectual-co:viabilidad-de-marca`. **El nombre en cámara de comercio no protege la marca** |
| Política de tratamiento de datos y RNBD | SIC | Ver `/datos-personales-co:politica-y-aviso` |
| Evaluación SAGRILAFT / PTEE | | Ver `/cumplimiento-co:diagnostico-de-obligados` |

**La confusión más costosa del arranque:** creer que registrar el nombre en la cámara de
comercio protege la marca. No la protege. Son registros distintos ante autoridades
distintas.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Constitución — [nombre proyectado]

### Tipo recomendado
**[SAS / SRL / SA / sucursal]** — porque [dos líneas]

### Comparación aplicada al caso
| Criterio | [Tipo A] | [Tipo B] | Cuál conviene aquí |
|---|---|---|---|

### Decisiones estructurales
| Decisión | Adoptada | Alternativa | Por qué |
|---|---|---|---|

### Advertencias
[desestimación art. 42, abuso del voto art. 43, responsabilidad de administradores,
homonimia, actividad vigilada]

---
[DOCUMENTO DE CONSTITUCIÓN Y ESTATUTOS]
---

### Trámites posteriores
| Trámite | Ante quién | Plazo | Responsable |
|---|---|---|---|

### Campos por diligenciar

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Verificar homonimia en el RUES antes de fijar el nombre.** Y advertir que el registro
  mercantil no da derechos marcarios.
- **Si la actividad es vigilada, decirlo antes de escoger el tipo:** puede haber capital
  mínimo, tipo obligatorio y autorización previa.
- **Si hay más de un socio, no entregar estatutos sin plantear las cláusulas de salida.**
  Es lo que evita el conflicto societario de dentro de tres años.

## Lo que esta skill NO hace

- No inscribe ni tramita.
- No verifica homonimia ni disponibilidad de nombre: indica que hay que hacerlo.
- No da asesoría tributaria sobre el vehículo: remite a `/tributario-co`.
