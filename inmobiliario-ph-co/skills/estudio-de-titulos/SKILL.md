---
name: estudio-de-titulos
description: >
  Lee el folio de matrícula inmobiliaria anotación por anotación, reconstruye la tradición
  y emite concepto de saneamiento con riesgos y su mitigación. Actívela ante «estudio de
  títulos», «voy a comprar un inmueble», «revisa este certificado de tradición y
  libertad», «falsa tradición», «el inmueble tiene embargo», «¿este predio es sano?»,
  «hipoteca», «afectación a vivienda familiar».
---

# Estudio de títulos

**Antes de empezar.** Leer `~/.claude/plugins/config/claude-legal-colombia/inmobiliario-ph-co/CLAUDE.md`.
**Sin el certificado de tradición y libertad no hay estudio de títulos.** Si el usuario
no lo aporta, pedirlo antes de cualquier análisis.

## Paso 1 — Los documentos mínimos

| Documento | Para qué | Vigencia |
|---|---|---|
| **Certificado de tradición y libertad (folio de matrícula)** | Es la columna vertebral del estudio | No mayor a 30 días |
| **Escrituras públicas** de la cadena de tradición | Verificar lo que dice el folio contra el título | Las del período estudiado |
| **Certificado catastral / boletín de nomenclatura** | Identificación del predio, avalúo, área | Reciente |
| **Paz y salvo de impuesto predial y de valorización** | Los impuestos gravan el inmueble | Reciente |
| **Paz y salvo de administración** (si es PH) | Las expensas siguen al inmueble (Ley 675, art. 29) | Reciente |
| **Certificado de existencia y representación** del vendedor persona jurídica | Facultades para enajenar | 30 días |
| **Registro civil de matrimonio o declaración de unión marital** | Afectación a vivienda familiar, sociedad conyugal | |
| **Reglamento de propiedad horizontal** | Si aplica | |
| **Licencias urbanísticas** | Si hay construcción reciente | |

## Paso 2 — Cuántos años se estudian

La práctica colombiana usa **10 años** como mínimo y **20 años** cuando el negocio lo
justifica o hay hallazgos.

**Razón jurídica del corte:** la prescripción adquisitiva extraordinaria es de **10 años**
(CC art. 2532, mod. Ley 791 de 2002), y la acción ordinaria prescribe en **10 años**
(CC art. 2536). Estudiar veinte da margen frente a nulidades y a situaciones no
consolidadas.

**Registrar en el concepto cuántos años se estudiaron y por qué.** Un estudio de cinco
años presentado sin advertencia es un estudio incompleto que compromete al abogado.

## Paso 3 — Lectura del folio, anotación por anotación

Para cada anotación se registra: número, fecha, naturaleza del acto, título (escritura
n.º, notaría, fecha), personas que intervienen, y **si está vigente o cancelada**.

### Lo que hay que buscar

| Hallazgo | Qué significa | Gravedad |
|---|---|---|
| **Falsa tradición** | Se transfirió un derecho incompleto: venta de cosa ajena, posesión, derechos hereditarios sin adjudicación. **El folio de falsa tradición no acredita dominio pleno** | 🔴 |
| **Embargo vigente** | El inmueble está fuera del comercio para efectos de la enajenación oponible | 🔴 |
| **Demanda inscrita** | Hay litigio sobre el inmueble | 🔴 |
| **Hipoteca vigente** | Gravamen. Debe cancelarse o subrogarse | 🟠 |
| **Patrimonio de familia inembargable** | Limita la disposición; requiere autorización judicial en ciertos supuestos `[verificar]` | 🟠 |
| **Afectación a vivienda familiar** (Ley 258 de 1996) | **Requiere el consentimiento de ambos cónyuges o compañeros** para enajenar o gravar | 🟠 |
| **Condición resolutoria** pendiente o **pacto de retroventa** | El dominio puede volver | 🟠 |
| **Sucesión no liquidada** | Los herederos no tienen dominio individual mientras no haya partición y adjudicación registrada | 🔴 |
| **Servidumbres** | Limitan el uso | 🟡 |
| **Limitaciones urbanísticas, zonas de protección, afectaciones viales** | Pueden impedir el uso proyectado | 🟠 |
| **Cambio de nomenclatura o de área sin explicación** | Puede indicar englobe, desenglobe o error registral | 🟠 |
| **Sociedad conyugal ilíquida** | El bien puede ser social aunque figure a nombre de uno | 🟠 |
| **Cancelaciones sin soporte** | Verificar contra la escritura | 🟠 |
| **Saltos en la cadena** | Un titular que no adquirió de quien figura como anterior | 🔴 |
| **Poderes** en la cadena | Verificar vigencia y facultades expresas para enajenar | 🟠 |
| **Adquisición por prescripción** | Verificar que haya sentencia registrada | 🟡 |
| **Bienes de origen sospechoso** | Extinción de dominio: verificar antecedentes | 🔴 |

### La verificación de la cadena

Se reconstruye hacia atrás: **cada titular debe haber adquirido de quien figuraba como
titular anterior.** Cualquier salto es un 🔴 hasta que se explique.

**Verificaciones sobre cada transferencia:**
- ¿Quien vendió tenía capacidad y facultades? (poderes, representación legal, autorización
  de junta o asamblea)
- ¿Se requería autorización judicial? (menores, personas con apoyos, patrimonio de
  familia)
- ¿Comparecieron ambos cónyuges cuando había afectación a vivienda familiar o sociedad
  conyugal?
- ¿La escritura se registró y en qué fecha? **El dominio se transfiere con el registro**,
  no con la escritura (CC art. 756).

## Paso 4 — Riesgos que el folio no muestra

El folio no dice todo. Advertirlo siempre:

| Riesgo | Cómo se verifica |
|---|---|
| **Poseedores u ocupantes** | Visita al inmueble. Un poseedor con más de 10 años puede prescribir |
| **Arrendatarios** | El arrendamiento se respeta frente al nuevo dueño en los términos de la ley |
| **Servidumbres de hecho** | Visita |
| **Diferencias entre el área registral, la catastral y la real** | Levantamiento topográfico |
| **Estado físico y estructural** | Peritaje |
| **Procesos en curso no inscritos** | Consulta de procesos judiciales |
| **Deudas de servicios públicos** | Certificados de las empresas |
| **Extinción de dominio en trámite** | Puede no estar inscrita en las primeras etapas |
| **Situación urbanística real** | Certificado de uso del suelo, POT |

**La visita al inmueble no es opcional.** Un estudio de títulos hecho solo sobre papeles
no detecta al poseedor que lleva doce años.

## Paso 5 — El concepto

Tres conclusiones posibles, y hay que escoger una:

| Conclusión | Significado |
|---|---|
| **Título sano** | Puede adquirirse. Se listan las verificaciones hechas y las advertencias |
| **Título saneable** | Hay hallazgos que pueden corregirse antes de la escritura. Se dice **cómo, quién y en qué orden** |
| **Título no sano** | No se recomienda adquirir, o solo bajo condiciones que se explican |

**No emitir conceptos ambiguos.** «Presenta algunos riesgos que deben evaluarse» no le
sirve a nadie y no protege al abogado.

## Salida

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO]

## Estudio de títulos — Matrícula [n.º] — [dirección]

### Conclusión
**[TÍTULO SANO / SANEABLE / NO SANO]**

### Alcance del estudio
| Punto | Contenido |
|---|---|
| Período estudiado | [N] años, desde la anotación [n.º] del [fecha] |
| Documentos revisados | |
| Documentos NO revisados | **[y qué riesgo queda abierto por ello]** |
| Fecha del certificado de tradición | |
| ¿Se visitó el inmueble? | **[no — advertencia expresa]** |

### Identificación del inmueble
| Dato | Folio | Catastro | Escritura | ¿Coinciden? |
|---|---|---|---|---|
| Dirección | | | | |
| Área | | | | |
| Linderos | | | | |

### Cadena de tradición
| Anot. | Fecha | Acto | Título | De | A | Observación |
|---|---|---|---|---|---|---|

### Gravámenes, limitaciones y medidas vigentes
| Anot. | Naturaleza | Beneficiario | Estado | Cómo se levanta |
|---|---|---|---|---|

### 🔴 Hallazgos
| # | Hallazgo | Anotación | Gravedad | Efecto | Saneamiento |
|---|---|---|---|---|---|

### Riesgos no verificables en el folio
| Riesgo | Cómo verificarlo | ¿Se verificó? |
|---|---|---|

### Condiciones para la escritura
1. [qué debe estar hecho antes de firmar]
2. [quién debe comparecer]
3. [qué debe decir la escritura]

### Recomendaciones de estructuración
[retención del precio hasta el registro, fiducia de pago, garantías, declaraciones del
vendedor, encargo fiduciario]

Fuentes: […] | Marcas pendientes: [N] | Revisó: [PENDIENTE DE REVISIÓN PROFESIONAL]
```

## Compuertas

- **Sin certificado de tradición vigente, no hay estudio.**
- **Decir siempre cuántos años se estudiaron.**
- **Falsa tradición, embargo, demanda inscrita, sucesión no liquidada y saltos en la
  cadena son 🔴** y encabezan el concepto.
- **Advertir expresamente lo que el folio no muestra** y que no se visitó el inmueble, si
  no se visitó.
- **El dominio se transfiere con el registro:** recordarlo al estructurar el pago.

## Lo que esta skill NO hace

- No consulta el registro ni obtiene certificados.
- No visita el inmueble ni hace levantamientos.
- No verifica antecedentes de extinción de dominio.
