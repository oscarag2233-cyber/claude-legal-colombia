# Claude Legal Colombia

Agentes, skills y conectores de referencia para el ejercicio del Derecho **en
Colombia**. Diecinueve plugins que cubren civil y comercial, responsabilidad civil,
familia y sucesiones, inmobiliario y propiedad horizontal, insolvencia, consumidor y
competencia, datos personales, laboral y seguridad social, societario, litigio civil,
contencioso administrativo y contratación estatal, cumplimiento, tributario, propiedad
intelectual, regulatorio, gobernanza de IA, y la formación jurídica —estudiantes y
consultorios—.

Construido tomando como modelo [`anthropics/claude-for-legal`](https://github.com/anthropics/claude-for-legal),
reescrito de raíz para **normativa y jurisprudencia colombianas**: Código Civil, Código
de Comercio, CST, CGP, CPACA, Estatuto Tributario, Decisiones Andinas, y la doctrina de
la Corte Constitucional, la Corte Suprema y el Consejo de Estado.

> [!IMPORTANT]
> **Todo lo que producen estos plugins es un borrador sujeto a revisión profesional —
> no es asesoría jurídica, no es concepto y no reemplaza a un abogado.**
> En Colombia el ejercicio de la abogacía está reservado a quien tiene tarjeta
> profesional vigente (Decreto 196 de 1971; Ley 1123 de 2007). La responsabilidad
> profesional por cualquier pieza que salga de aquí es del abogado que la revisa, la
> suscribe y la radica. Lea [AVISO-LEGAL.md](AVISO-LEGAL.md) antes de usar esto en un
> expediente real.

## Qué lo hace distinto de traducir el repositorio original

El derecho no se traduce; se reescribe. Estos plugins no son la versión en español de
un modelo estadounidense:

| Decisión de diseño | Por qué |
|---|---|
| **Verificación de fuentes como compuerta, no como recomendación** | La fabricación de citas es el riesgo número uno del uso de IA en Derecho. Cada plugin trae una skill `verificar-citas` que bloquea la radicación cuando una cita que sostiene una conclusión no se pudo confirmar en fuente oficial |
| **Etiquetas de procedencia obligatorias** | `[conocimiento del modelo — verificar]` es el valor por defecto. Una cita solo se declara verificada si apareció en un resultado de fuente oficial **en esta sesión** |
| **Términos con la norma a la vista** | Ningún término sale como número suelto: sale con el artículo que lo fija, si corre en hábiles o calendario, el día de inicio y su razón, y la advertencia de contrastar contra el calendario judicial |
| **Secreto profesional, no *work product*** | El encabezado de producto de trabajo se calibró al régimen colombiano: la reserva del art. 74 de la Constitución no equivale a la doctrina estadounidense, y no protege documentos exigibles en visita administrativa |
| **Compuerta de revisión profesional** | Si quien usa el plugin no es abogado inscrito, ninguna skill deja pasar un acto con consecuencias jurídicas sin un alto explícito |
| **Vigencia normativa como problema de primer orden** | Cada perfil trae su tabla de marco normativo con estado de verificación, y el disparador de actualidad obliga a buscar antes de responder cuando algo depende de una reforma o de un umbral anual |
| **Detección de conflicto de interés** | Los espacios de asunto cotejan las partes de cada caso nuevo contra los existentes y se detienen ante una posible colisión (Ley 1123 de 2007, art. 34) |

## Instalación

```bash
/plugin marketplace add oscarag2233-cyber/claude-legal-colombia
```

Luego instale los plugins del área en que trabaje:

```bash
/plugin install litigio-civil-co@claude-legal-colombia
/plugin install laboral-seguridad-social-co@claude-legal-colombia
```

Y **corra siempre la entrevista inicial** antes de pedirle nada:

```bash
/litigio-civil-co:entrevista-inicial
```

Sin ella, las skills se detienen. Prefieren no responder a responder genérico.

Ver [INICIO-RAPIDO.md](INICIO-RAPIDO.md) para la ruta de 60 segundos.

## Los plugins

| Plugin | Área | Qué resuelve |
|---|---|---|
| [`consultorio-juridico-co`](consultorio-juridico-co/) | Consultorio Jurídico | entrevista y ficha de consulta, concepto para el usuario en lenguaje claro, control de términos con criterio de prevención del daño, cola de… |
| [`consumidor-competencia-co`](consumidor-competencia-co/) | Consumidor y Competencia | garantía legal y calidad e idoneidad, demandas de protección al consumidor, publicidad engañosa y cláusulas abusivas, prácticas comerciales… |
| [`contencioso-administrativo-co`](contencioso-administrativo-co/) | Contencioso Administrativo y Contratación Estatal | escoge el medio de control y controla la caducidad, agota vía gubernativa y conciliación prejudicial, arma nulidad y restablecimiento y reparación… |
| [`contratos-comercial-co`](contratos-comercial-co/) | Contratos y Derecho Comercial | califica el tipo contractual, contrasta el clausulado contra los criterios de la casa, marca cláusulas abusivas y de riesgo, analiza… |
| [`cumplimiento-co`](cumplimiento-co/) | Cumplimiento — SAGRILAFT, PTEE y Antisoborno | SAGRILAFT y PTEE bajo la Circular Básica Jurídica de la Superintendencia de Sociedades, responsabilidad administrativa por soborno transnacional… |
| [`datos-personales-co`](datos-personales-co/) | Datos Personales y Habeas Data | evaluación del tratamiento, política y aviso de privacidad, atención de consultas y reclamos en los términos de la Ley 1581 de 2012, gestión de… |
| [`estudiante-derecho-co`](estudiante-derecho-co/) | Estudiante de Derecho | ficha sentencias separando ratio de obiter, interroga con método socrático, enseña a construir líneas jurisprudenciales, prepara exámenes y… |
| [`familia-sucesiones-co`](familia-sucesiones-co/) | Familia y Sucesiones | alimentos, custodia y visitas bajo el interés superior del menor, divorcio y liquidación de la sociedad conyugal o patrimonial, unión marital de… |
| [`gobernanza-ia-co`](gobernanza-ia-co/) | Gobernanza de Inteligencia Artificial | inventario de sistemas, triage de casos de uso por riesgo, evaluación de impacto que cruza protección de datos y derechos fundamentales, política… |
| [`hub-constructor-legal-co`](hub-constructor-legal-co/) | Hub de Constructores Legales | Encuentra, evalúa e instala skills jurídicas de la comunidad con una compuerta de revisión de seguridad y calidad jurídica |
| [`inmobiliario-ph-co`](inmobiliario-ph-co/) | Inmobiliario y Propiedad Horizontal | estudio de títulos con lectura de folio de matrícula, contratos de compraventa y arrendamiento urbano bajo la Ley 820 de 2003, restitución de… |
| [`insolvencia-co`](insolvencia-co/) | Insolvencia y Reorganización | Diagnostica si la empresa o la persona natural está en los supuestos de insolvencia, prepara la solicitud de reorganización o de liquidación… |
| [`laboral-seguridad-social-co`](laboral-seguridad-social-co/) | Laboral y Seguridad Social | liquidación de prestaciones e indemnizaciones, terminación con y sin justa causa, procedimiento disciplinario con debido proceso, tipo de… |
| [`litigio-civil-co`](litigio-civil-co/) | Litigio Civil y Comercial | competencia y viabilidad, demanda que no se inadmite, contestación con excepciones bien planteadas, plan probatorio, ejecutivo, medidas… |
| [`propiedad-intelectual-co`](propiedad-intelectual-co/) | Propiedad Intelectual | viabilidad y registro de marca ante la SIC con análisis de confundibilidad, oposiciones y cancelaciones, derecho de autor y registro de software… |
| [`regulatorio-co`](regulatorio-co/) | Regulatorio y Vigilancia Normativa | vigilancia del Diario Oficial, de las superintendencias y de las altas cortes, análisis de impacto de una norma nueva sobre las obligaciones… |
| [`responsabilidad-civil-co`](responsabilidad-civil-co/) | Responsabilidad Civil y Seguros | identifica el régimen aplicable, prueba los elementos, liquida perjuicios materiales e inmateriales con las fórmulas usadas por los jueces… |
| [`societario-co`](societario-co/) | Societario | elección de tipo societario y constitución de SAS, convocatoria y desarrollo de asambleas con actas que resistan impugnación, reformas… |
| [`tributario-co`](tributario-co/) | Tributario | revisión de declaraciones y correcciones, respuesta a requerimientos especiales y pliegos, recurso de reconsideración, procedimiento… |

## Cómo está armado cada plugin

```
<plugin>/
  .claude-plugin/plugin.json   # manifiesto
  .mcp.json                    # servidores MCP que el plugin sugiere
  CLAUDE.md                    # PLANTILLA del perfil de práctica (no es contexto del proyecto)
  README.md                    # documentación del plugin
  skills/<nombre>/SKILL.md     # una skill por directorio
  agents/<nombre>.md           # agentes programados
  hooks/hooks.json             # ganchos (la mayoría vienen vacíos)
```

**Cuatro skills están en todos los plugins:**

| Skill | Qué hace |
|---|---|
| `entrevista-inicial` | Levanta el perfil de práctica, los criterios de la casa y el escalamiento. Es la única que corre sin configuración |
| `personalizar` | Ajusta el perfil sin repetir la entrevista |
| `verificar-citas` | Compuerta de verificación de normas, sentencias, términos y cifras contra fuente oficial |
| `espacio-de-asunto` | Aísla contexto y salidas por caso, con detección de conflicto de interés |

## Referencias compartidas

El material que usan todos los plugins vive en [`referencias/`](referencias/):

| Archivo | Contenido |
|---|---|
| [`verificacion-de-fuentes.md`](referencias/verificacion-de-fuentes.md) | La regla dura del repositorio: tres valores, etiquetas de procedencia, disparador de actualidad |
| [`fuentes-oficiales.md`](referencias/fuentes-oficiales.md) | Catálogo de fuentes oficiales colombianas y convención de citación |
| [`jerarquia-normativa.md`](referencias/jerarquia-normativa.md) | Jerarquía, bloque de constitucionalidad, derecho andino, efectos de las decisiones de la Corte |
| [`precedente-y-jurisprudencia.md`](referencias/precedente-y-jurisprudencia.md) | Ratio y obiter, precedente vertical y horizontal, doctrina probable, líneas jurisprudenciales |
| [`terminos-caducidad-prescripcion.md`](referencias/terminos-caducidad-prescripcion.md) | Cómputo de términos, caducidad del CPACA, prescripción civil, comercial y laboral |
| [`cuantificacion-de-perjuicios.md`](referencias/cuantificacion-de-perjuicios.md) | Tipología del daño, topes de la unificación de 2014 y fórmulas de lucro cesante |
| [`estructura-de-escritos.md`](referencias/estructura-de-escritos.md) | Requisitos de demanda, contestación, tutela, petición y recursos |
| [`valores-anuales.md`](referencias/valores-anuales.md) | SMLMV, UVT y todo lo que cambia cada año |
| [`tratamiento-de-datos.md`](referencias/tratamiento-de-datos.md) | Cómo manejar datos de clientes antes de procesarlos |
| [`ia-y-judicatura.md`](referencias/ia-y-judicatura.md) | Uso de IA en actuaciones judiciales y deberes profesionales |

## Cookbooks de agentes

[`cookbooks-agentes/`](cookbooks-agentes/) trae recetas de agentes programados —vigía
de términos, vigía normativo, vigía de renovaciones— con su orquestador, sus subagentes
y el alcance de herramientas de cada uno.

## Validación

```bash
python3 scripts/validar.py
```

Comprueba las invariantes del manifiesto, el frontmatter de skills y agentes, la
coherencia entre `marketplace.json` y cada `plugin.json`, y que toda referencia
`/plugin:skill` que aparezca en prosa apunte a una skill que exista.

Para regenerar el andamiaje común después de tocar el registro:

```bash
python3 scripts/generar-comunes.py
```

## Estado y alcance

Este repositorio es **material de trabajo, no doctrina**. Las tablas de marco normativo
son un punto de partida verificable, no una fuente. Cada una trae su casilla de estado
de verificación precisamente porque nadie —ni el modelo ni el autor— debe presentarlas
como confirmadas sin haberlas confirmado.

Si encuentra una norma mal citada, una vigencia equivocada o una posición
jurisprudencial superada, abra un issue. Ver [CONTRIBUIR.md](CONTRIBUIR.md).

## Licencia

[MIT](LICENSE).
