# -*- coding: utf-8 -*-
"""Registro único de plugins de claude-legal-colombia.

Fuente de verdad para marketplace.json, plugin.json, README y CLAUDE.md de cada
plugin. Editar aquí y correr `python3 scripts/generar-comunes.py`.
"""

MARKETPLACE = {
    "name": "claude-legal-colombia",
    "description": (
        "Agentes, skills y conectores de referencia para el ejercicio del Derecho en "
        "Colombia: civil y comercial, responsabilidad civil, familia y sucesiones, "
        "inmobiliario y propiedad horizontal, insolvencia, consumidor y competencia, "
        "datos personales, laboral y seguridad social, societario, litigio civil, "
        "contencioso administrativo y contratación estatal, cumplimiento, tributario, "
        "propiedad intelectual, regulatorio, gobernanza de IA, y la formación jurídica "
        "(estudiantes y consultorios). Construido sobre normativa y jurisprudencia "
        "colombianas, con verificación obligatoria de fuentes."
    ),
    "owner": {"name": "Oscar Gutiérrez Saavedra"},
    "author": {"name": "Oscar Gutiérrez Saavedra"},
}

# Catálogo compartido de servidores MCP (URLs de proveedores; los conectores
# colombianos se documentan en CONECTORES.md).
MCP = {
    "drive": ("Google Drive", "https://drivemcp.googleapis.com/mcp/v1",
              "Buscar, leer y traer documentos de Google Drive."),
    "box": ("Box", "https://mcp.box.com/mcp",
            "Acceso gobernado a documentos almacenados en Box."),
    "slack": ("Slack", "https://mcp.slack.com/mcp",
              "Buscar mensajes y canales del espacio de trabajo."),
    "docusign": ("DocuSign", "https://mcp.docusign.com/mcp",
                 "Búsqueda de acuerdos, estado de firma y flujos de suscripción."),
    "imanage": ("iManage", "https://cloudimanage.com/mcp/work",
                "Contenido gobernado de iManage: los documentos permanecen en iManage."),
    "atlassian": ("Atlassian", "https://mcp.atlassian.com/v1/sse",
                  "Jira y Confluence: seguimiento de tareas y base de conocimiento."),
    "asana": ("Asana", "https://mcp.asana.com/sse",
              "Seguimiento de tareas y proyectos del equipo."),
    "linear": ("Linear", "https://mcp.linear.app/mcp",
               "Seguimiento de incidencias y proyectos de producto."),
}

CATEGORIAS = {
    "documentos": ["documents", "legal-document-management"],
    "firma": ["e-signature"],
    "correo": ["email", "chat"],
    "gestion": ["case-management", "project-management"],
    "contratos": ["contract-management", "contract-review"],
    "investigacion": ["legal-research", "case-law"],
    "regulatorio": ["regulatory-intelligence"],
    "pi": ["ip-management"],
    "gobierno": ["board-governance"],
}

PLUGINS = [
 {
  "slug": "contratos-comercial-co",
  "display": "Contratos y Derecho Comercial",
  "desc": ("Revisa y redacta contratos civiles y mercantiles bajo el Código Civil y el "
           "Código de Comercio: califica el tipo contractual, contrasta el clausulado "
           "contra los criterios de la casa, marca cláusulas abusivas y de riesgo, "
           "analiza incumplimiento y remedios, y traduce la revisión a un resumen que el "
           "cliente o el área de negocio sí lee."),
  "ambito": "Contratación civil y mercantil, obligaciones, garantías y remedios contractuales.",
  "normas": [
    ("Código Civil (Ley 84 de 1873)", "Obligaciones y contratos: arts. 1494 y ss., 1502 (requisitos), 1602 (fuerza obligatoria), 1603 (buena fe), 1616 (previsibilidad), 1546 (condición resolutoria tácita)"),
    ("Código de Comercio (Decreto 410 de 1971)", "Actos de comercio, contratos mercantiles típicos, art. 822 (remisión al civil), art. 830 (abuso del derecho), art. 871 (buena fe), art. 884 (intereses)"),
    ("Ley 1480 de 2011", "Estatuto del Consumidor: aplica cuando una parte es consumidor; cláusulas abusivas, garantía legal"),
    ("Ley 527 de 1999", "Comercio electrónico, mensajes de datos y firmas electrónicas"),
    ("Decreto 1074 de 2015", "Decreto Único Reglamentario del sector Comercio, Industria y Turismo"),
    ("Ley 2213 de 2022", "Mensajes de datos y actuaciones electrónicas"),
  ],
  "autoridades": ["Superintendencia de Industria y Comercio (consumidor y competencia)",
                  "Superintendencia de Sociedades (facultades jurisdiccionales)",
                  "Jueces civiles del circuito y municipales",
                  "Centros de conciliación y tribunales de arbitramento"],
  "integraciones": [
    ("Gestor documental (Drive / Box / SharePoint)", "El usuario adjunta el contrato en cada revisión"),
    ("Firma electrónica", "El usuario tramita la firma por fuera del plugin"),
    ("Gestor de contratos o carpeta de minutas", "Se lleva un registro local de vencimientos y renovaciones"),
    ("Correo y calendario", "Las alertas se entregan en línea en lugar de agendarse"),
  ],
  "mcp": ["drive", "box", "docusign", "imanage", "slack"],
  "cats": ["contratos", "documentos", "firma", "correo"],
  "propias": [
    ("revisar-contrato", "Revisión cláusula por cláusula contra los criterios de la casa, con marcación de desviaciones y propuesta de redlines quirúrgicos."),
    ("minutar-contrato", "Redacta o adapta una minuta a partir del negocio real, con las cláusulas que el tipo contractual exige y las que la práctica colombiana espera."),
    ("clausulas-de-riesgo", "Barrido específico de cláusulas abusivas, penales excesivas, limitaciones de responsabilidad inválidas y pactos que no resisten el control judicial."),
    ("incumplimiento-y-remedios", "Califica el incumplimiento y mapea los remedios disponibles con sus requisitos, términos y costo procesal."),
    ("resumen-para-el-negocio", "Traduce la revisión a un resumen accionable para quien decide, sin perder las advertencias jurídicas."),
  ],
  "agentes": [("vigia-renovaciones", "Revisa el registro de contratos y avisa qué vence o se renueva automáticamente antes de que se cierre la ventana de preaviso.")],
  "criterios": """### Posiciones de la casa por cláusula

*Cada posición tiene tres niveles: estándar, alternativa aceptable y nunca. Si una
casilla dice `[PENDIENTE]`, la skill correspondiente debe preguntar antes de
calificar, no asumir.*

#### Limitación de responsabilidad
**Estándar:** [PENDIENTE — p. ej. «tope al valor del contrato en los últimos 12 meses»]
**Alternativas aceptables:** [PENDIENTE]
**Nunca:** [PENDIENTE — p. ej. «exoneración por dolo o culpa grave», que además es nula (CC art. 1522, 1604 y 63)]

*Recordatorio de derecho imperativo: la condonación del dolo futuro no vale
(CC art. 1522) y la cláusula que exonera de culpa grave se asimila al dolo (CC art. 63).
Ningún criterio de la casa puede autorizar lo que la ley prohíbe.*

#### Cláusula penal
**Estándar:** [PENDIENTE]
**Tope:** la pena no puede exceder el duplo de la obligación principal en las
obligaciones de cantidad determinada (CC art. 1601), y es reducible si hay
cumplimiento parcial (CC art. 1596).
**Nunca:** [PENDIENTE]

#### Terminación
**Estándar:** [PENDIENTE — preaviso, causales, terminación unilateral]
**Nunca:** [PENDIENTE]

#### Ley aplicable y solución de controversias
**Preferida:** [PENDIENTE — jurisdicción ordinaria / arbitraje / centro y número de árbitros]
**Aceptable:** [PENDIENTE]
**Nunca:** [PENDIENTE]

#### Cesión, confidencialidad y protección de datos
**Estándar:** [PENDIENTE]

#### Lo único innegociable
[PENDIENTE — la posición que se revisa de primera en todo contrato]
""",
  "preferencias": """## Preferencias de revisión contractual

**Profundidad por defecto:** [PENDIENTE — barrido rápido / cláusula por cláusula]
**Formato de redline:** [PENDIENTE — tabla comparativa / texto con marcas / documento aparte]
**Acción de cierre:** [PENDIENTE — texto que se añade al final de toda revisión]
""",
 },
 {
  "slug": "responsabilidad-civil-co",
  "display": "Responsabilidad Civil y Seguros",
  "desc": ("Analiza responsabilidad civil contractual y extracontractual bajo el Código "
           "Civil y la jurisprudencia de la Sala Civil: identifica el régimen aplicable, "
           "prueba los elementos, liquida perjuicios materiales e inmateriales con las "
           "fórmulas usadas por los jueces colombianos, gestiona la reclamación al "
           "asegurador y evalúa la viabilidad del litigio antes de demandar."),
  "ambito": "Responsabilidad civil contractual y extracontractual, actividades peligrosas, responsabilidad médica y de tránsito, seguros de daños y de responsabilidad.",
  "normas": [
    ("Código Civil, arts. 2341 a 2360", "Responsabilidad extracontractual: hecho propio, hecho ajeno, cosas y actividades peligrosas (art. 2356)"),
    ("Código Civil, arts. 1613 a 1616", "Perjuicios contractuales: daño emergente, lucro cesante, previsibilidad"),
    ("Código Civil, art. 2357", "Reducción por concurrencia de culpas de la víctima"),
    ("Código de Comercio, arts. 1036 a 1162", "Contrato de seguro; art. 1077 (carga de la prueba), art. 1080 (plazo de pago del siniestro), art. 1081 (prescripción)"),
    ("Código de Comercio, arts. 1127 y ss.", "Seguro de responsabilidad civil y acción directa de la víctima (art. 1133)"),
    ("Ley 769 de 2002", "Código Nacional de Tránsito; SOAT y responsabilidad por accidentes de tránsito"),
    ("Ley 1564 de 2012", "CGP: juramento estimatorio (art. 206), prueba pericial, medidas cautelares"),
  ],
  "autoridades": ["Jueces civiles municipales y del circuito",
                  "Corte Suprema de Justicia, Sala de Casación Civil",
                  "Superintendencia Financiera (conducta de aseguradoras)",
                  "Defensor del Consumidor Financiero"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta historia clínica, informes de tránsito o pericias en cada análisis"),
    ("Consulta de procesos de la Rama Judicial", "El seguimiento del proceso se hace manualmente"),
    ("Hoja de cálculo para liquidaciones", "La liquidación se entrega en tabla dentro de la respuesta"),
  ],
  "mcp": ["drive", "box", "slack"],
  "cats": ["documentos", "gestion", "investigacion"],
  "propias": [
    ("analisis-de-responsabilidad", "Determina el régimen aplicable, mapea los elementos y evalúa las causales de exoneración con el sustrato probatorio disponible."),
    ("liquidar-perjuicios", "Liquida daño emergente, lucro cesante consolidado y futuro, y perjuicios inmateriales con memoria de cálculo completa."),
    ("reclamacion-a-aseguradora", "Arma la reclamación con la carga probatoria del art. 1077 del C.Co., controla el plazo del art. 1080 y evalúa la objeción del asegurador."),
    ("viabilidad-de-litigio", "Puntúa el caso antes de demandar: prueba, prescripción, solvencia del demandado, costo y escenarios de transacción."),
    ("demanda-de-responsabilidad", "Redacta la demanda con hechos numerados, juramento estimatorio razonado y plan probatorio coherente."),
  ],
  "agentes": [("vigia-prescripcion", "Revisa los casos abiertos y avisa cuáles se acercan a la prescripción o a la caducidad, con la norma del término a la vista.")],
  "criterios": """### Criterios de la casa

#### Umbral para asumir un caso
**Cuantía mínima estimada:** [PENDIENTE]
**Probabilidad mínima de éxito:** [PENDIENTE]
**Solvencia del demandado:** [PENDIENTE — cómo se verifica antes de demandar]

#### Postura sobre cuantificación
**Perjuicio moral — tope que usamos:** [PENDIENTE — recordar que el tope contencioso (hasta 100 SMLMV) no es el de la jurisdicción ordinaria]
**Actualización:** [PENDIENTE — IPC a la fecha de la liquidación]
**Juramento estimatorio:** [PENDIENTE — política de la casa; recordar la sanción del art. 206 CGP condicionada por la Sentencia C-157 de 2013]

#### Transacción
**Cuándo se recomienda transar:** [PENDIENTE]
**Rango de descuento aceptable:** [PENDIENTE]

#### Lo único innegociable
[PENDIENTE]
""",
  "preferencias": """## Preferencias de análisis

**Nivel de detalle de la liquidación:** [PENDIENTE — resumen / memoria completa]
**Tablas de vida probable:** Resolución 1555 de 2010 de la Superintendencia Financiera `[verificar tabla vigente]`
**Interés técnico:** 0,004867 mensual `[verificar]`
""",
 },
]

PLUGINS += [
 {
  "slug": "familia-sucesiones-co",
  "display": "Familia y Sucesiones",
  "desc": ("Trabaja los asuntos de familia y sucesorios con el cuidado que exigen: alimentos, "
           "custodia y visitas bajo el interés superior del menor, divorcio y liquidación de la "
           "sociedad conyugal o patrimonial, unión marital de hecho, y sucesiones notariales y "
           "judiciales. Incorpora las rutas de protección frente a violencia intrafamiliar y las "
           "reglas de capacidad de la Ley 1996 de 2019."),
  "ambito": "Derecho de familia, infancia y adolescencia, régimen económico de la pareja y derecho sucesoral.",
  "normas": [
    ("Código Civil, Libro I y Libro III", "Familia, matrimonio, filiación, sucesiones y particiones"),
    ("Ley 1098 de 2006", "Código de la Infancia y la Adolescencia: interés superior, custodia, alimentos, restablecimiento de derechos"),
    ("Ley 25 de 1992", "Divorcio del matrimonio civil y cesación de efectos civiles del religioso"),
    ("Ley 54 de 1990, modificada por la Ley 979 de 2005", "Unión marital de hecho y sociedad patrimonial entre compañeros permanentes"),
    ("Ley 1564 de 2012", "CGP: procesos de familia, sucesión (arts. 487 y ss.), verbal sumario"),
    ("Decreto 902 de 1988", "Sucesión ante notario cuando hay acuerdo entre herederos capaces"),
    ("Ley 1996 de 2019", "Régimen de capacidad legal de personas con discapacidad; sustituye la interdicción por apoyos"),
    ("Ley 294 de 1996 y Ley 1257 de 2008", "Violencia intrafamiliar y violencia contra la mujer: medidas de protección"),
    ("Ley 1361 de 2009", "Protección integral a la familia"),
  ],
  "autoridades": ["Jueces de familia y promiscuos de familia", "Comisarías de Familia",
                  "Defensorías de Familia (ICBF)", "Notarías (sucesión y divorcio de mutuo acuerdo)",
                  "Corte Constitucional (línea de interés superior del menor)"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta registros civiles y pruebas en cada consulta"),
    ("Calendario", "Los términos y audiencias se entregan en tabla, sin agendar"),
  ],
  "mcp": ["drive", "slack"],
  "cats": ["documentos", "gestion"],
  "propias": [
    ("alimentos", "Fija o revisa la cuota alimentaria con capacidad económica, necesidad y concurrencia de obligados, y arma la ruta de exigibilidad."),
    ("custodia-y-visitas", "Estructura el acuerdo o la demanda de custodia y régimen de visitas aplicando el interés superior del menor como criterio operativo, no como frase."),
    ("divorcio-y-liquidacion", "Escoge la causal o la vía de mutuo acuerdo, y liquida la sociedad conyugal o patrimonial con inventario, avalúos y adjudicación."),
    ("sucesion", "Arma la sucesión notarial o judicial: acervo, órdenes hereditarios, asignaciones forzosas, porción conyugal, colación y partición."),
    ("proteccion-frente-a-violencia", "Ruta de medidas de protección ante comisaría o juez, con lo que hay que probar y lo que se puede pedir el mismo día."),
  ],
  "agentes": [],
  "decisiones": ["Cuándo se recomienda la vía notarial frente a la judicial",
                 "Postura de la casa sobre acuerdos de custodia compartida",
                 "Umbral para remitir a un especialista en violencia intrafamiliar",
                 "Política sobre honorarios de éxito en asuntos de familia"],
  "sensible": True,
 },
 {
  "slug": "inmobiliario-ph-co",
  "display": "Inmobiliario y Propiedad Horizontal",
  "desc": ("Cubre la vida del inmueble: estudio de títulos con lectura de folio de matrícula, "
           "contratos de compraventa y arrendamiento urbano bajo la Ley 820 de 2003, restitución "
           "de inmueble arrendado, y la operación de la propiedad horizontal bajo la Ley 675 de "
           "2001 — asambleas, reglamento, cuotas, sanciones y conflictos entre copropietarios."),
  "ambito": "Derecho inmobiliario, registro, arrendamiento urbano y propiedad horizontal.",
  "normas": [
    ("Código Civil, Libro II", "Bienes, tradición, posesión, servidumbres, acciones reales"),
    ("Ley 1579 de 2012", "Estatuto de Registro de Instrumentos Públicos"),
    ("Ley 820 de 2003", "Arrendamiento de vivienda urbana: canon, reajuste, causales de terminación, restitución"),
    ("Ley 675 de 2001", "Régimen de propiedad horizontal: órganos, coeficientes, cuotas, sanciones, órgano de convivencia"),
    ("Ley 1564 de 2012", "CGP: restitución de inmueble arrendado (art. 384), pertenencia (art. 375), divisorios, ejecutivo por cuotas de administración"),
    ("Ley 388 de 1997", "Ordenamiento territorial, licencias y usos del suelo"),
    ("Decreto 1077 de 2015", "DUR de Vivienda, Ciudad y Territorio; licencias urbanísticas y curadurías"),
  ],
  "autoridades": ["Oficinas de Registro de Instrumentos Públicos", "Curadurías urbanas y secretarías de planeación",
                  "Jueces civiles municipales (restitución) y del circuito", "Alcaldías e inspecciones de policía (Ley 1801 de 2016)"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta folio de matrícula, escrituras y reglamento en cada análisis"),
    ("Consulta registral en línea", "El estudio se hace sobre el folio que aporte el usuario"),
  ],
  "mcp": ["drive", "box", "docusign"],
  "cats": ["documentos", "contratos", "firma"],
  "propias": [
    ("estudio-de-titulos", "Lee el folio de matrícula anotación por anotación, reconstruye la tradición y emite concepto de saneamiento con riesgos y su mitigación."),
    ("contrato-de-arrendamiento", "Redacta o revisa el arrendamiento distinguiendo vivienda urbana (imperativa) de comercial y de otros destinos."),
    ("restitucion-de-inmueble", "Arma el proceso de restitución con la causal correcta, los requisitos de procedibilidad y las cargas del arrendatario para ser oído."),
    ("asamblea-y-reglamento-ph", "Convoca, desarrolla y documenta la asamblea conforme a la Ley 675, y revisa el reglamento contra la norma imperativa."),
    ("conflictos-en-ph", "Resuelve el conflicto de copropiedad por la vía que corresponde: comité de convivencia, asamblea, policía o juez."),
  ],
  "agentes": [],
  "decisiones": ["Alcance por defecto del estudio de títulos (número de años de tradición)",
                 "Postura sobre garantías y depósitos en arrendamiento",
                 "Cuándo se recomienda proceso ejecutivo por cuotas de administración frente a acuerdo de pago"],
 },
 {
  "slug": "insolvencia-co",
  "display": "Insolvencia y Reorganización",
  "desc": ("Diagnostica si la empresa o la persona natural está en los supuestos de insolvencia, "
           "prepara la solicitud de reorganización o de liquidación judicial ante la "
           "Superintendencia de Sociedades bajo la Ley 1116 de 2006, revisa la calificación y "
           "graduación de créditos, negocia el acuerdo, y maneja la insolvencia de persona natural "
           "no comerciante ante centro de conciliación o notaría."),
  "ambito": "Régimen de insolvencia empresarial y de persona natural no comerciante.",
  "normas": [
    ("Ley 1116 de 2006", "Régimen de insolvencia empresarial: reorganización, liquidación judicial, validación de acuerdos extrajudiciales"),
    ("Ley 1564 de 2012, arts. 531 a 576", "Insolvencia de la persona natural no comerciante: negociación de deudas, convalidación y liquidación patrimonial"),
    ("Decreto 1074 de 2015", "Reglamentación del régimen de insolvencia; requisitos de la solicitud"),
    ("Ley 2069 de 2020", "Emprendimiento: ajustes al régimen de insolvencia y procesos de menor cuantía"),
    ("Código de Comercio, arts. 1 y ss.", "Calidad de comerciante, que determina el régimen aplicable"),
  ],
  "autoridades": ["Superintendencia de Sociedades (juez del concurso)", "Jueces civiles del circuito (en subsidio)",
                  "Centros de conciliación y notarías (insolvencia de persona natural)"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta estados financieros y relación de acreedores"),
    ("Hoja de cálculo", "Los inventarios y la graduación se entregan en tabla"),
  ],
  "mcp": ["drive", "box"],
  "cats": ["documentos", "gestion"],
  "propias": [
    ("diagnostico-de-insolvencia", "Determina si se configuran cesación de pagos o incapacidad de pago inminente, y cuál es el régimen y el juez competente."),
    ("solicitud-de-reorganizacion", "Arma la solicitud con los anexos que exige la ley y anticipa los requerimientos que suele hacer la Superintendencia."),
    ("calificacion-y-graduacion", "Revisa la calificación y graduación de créditos y prepara objeciones con soporte."),
    ("acuerdo-de-reorganizacion", "Estructura el acuerdo: clases de acreedores, mayorías, prelación legal y flujo de pagos sostenible."),
    ("insolvencia-persona-natural", "Ruta completa del procedimiento de negociación de deudas de persona natural no comerciante."),
  ],
  "agentes": [],
  "decisiones": ["Cuándo se recomienda reorganización frente a liquidación",
                 "Postura sobre acuerdos extrajudiciales de reorganización",
                 "Umbral de viabilidad financiera mínima para acompañar una reorganización"],
 },
 {
  "slug": "consumidor-competencia-co",
  "display": "Consumidor y Competencia",
  "desc": ("Trabaja el Estatuto del Consumidor y el régimen de competencia ante la SIC: garantía "
           "legal y calidad e idoneidad, demandas de protección al consumidor, publicidad engañosa "
           "y cláusulas abusivas, prácticas comerciales restrictivas y actos de competencia "
           "desleal, con la lógica de la actuación administrativa y de la jurisdiccional de la "
           "Superintendencia."),
  "ambito": "Protección al consumidor, publicidad, prácticas restrictivas de la competencia y competencia desleal.",
  "normas": [
    ("Ley 1480 de 2011", "Estatuto del Consumidor: garantía legal (arts. 7-8), calidad e idoneidad, información, publicidad, cláusulas abusivas (arts. 42-43), acción de protección al consumidor (art. 56 y ss.)"),
    ("Ley 155 de 1959 y Decreto 2153 de 1992", "Régimen general de competencia; acuerdos y abusos de posición dominante"),
    ("Ley 1340 de 2009", "Protección de la competencia: integraciones empresariales, beneficios por colaboración, caducidad"),
    ("Ley 256 de 1996", "Competencia desleal: cláusula general y actos típicos"),
    ("Decreto 1074 de 2015", "Reglamentación de consumidor y competencia"),
    ("Ley 2300 de 2023", "Protección frente a prácticas abusivas de cobranza"),
  ],
  "autoridades": ["Superintendencia de Industria y Comercio (Delegaturas de Protección al Consumidor, Competencia y Asuntos Jurisdiccionales)",
                  "Superintendencia Financiera y Defensor del Consumidor Financiero (sector financiero)",
                  "Jueces civiles (competencia a prevención en acción de protección al consumidor)"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta la factura, la publicidad o el contrato"),
    ("Correo", "Las reclamaciones se entregan como borrador para envío manual"),
  ],
  "mcp": ["drive", "slack"],
  "cats": ["documentos", "regulatorio"],
  "propias": [
    ("garantia-y-calidad", "Determina si hay incumplimiento de la garantía legal, quién responde solidariamente y cuál es el remedio que corresponde pedir."),
    ("demanda-de-proteccion-al-consumidor", "Redacta la demanda ante la SIC o el juez, con la pretensión correcta y la caducidad controlada."),
    ("publicidad-y-clausulas-abusivas", "Audita piezas publicitarias y clausulados de adhesión contra los arts. 29 a 33 y 42 a 43 de la Ley 1480."),
    ("practicas-restrictivas", "Evalúa riesgo de acuerdo restrictivo, abuso de posición dominante o integración que requiere autorización."),
    ("competencia-desleal", "Califica la conducta bajo la Ley 256 de 1996 y define la vía: jurisdiccional ante la SIC o ante el juez."),
  ],
  "agentes": [],
  "decisiones": ["Umbral para acudir a la SIC frente a la vía civil",
                 "Postura sobre programas de cumplimiento en competencia",
                 "Política de respuesta a requerimientos de la SIC"],
 },
 {
  "slug": "datos-personales-co",
  "display": "Datos Personales y Habeas Data",
  "desc": ("Implementa y sostiene el régimen colombiano de protección de datos: evaluación del "
           "tratamiento, política y aviso de privacidad, atención de consultas y reclamos en los "
           "términos de la Ley 1581 de 2012, gestión de incidentes de seguridad ante la SIC, "
           "transferencias y transmisiones internacionales, contratos de encargo y el régimen "
           "especial de dato financiero de la Ley 1266 de 2008."),
  "ambito": "Habeas data, protección de datos personales y dato financiero y crediticio.",
  "normas": [
    ("Constitución Política, arts. 15 y 20", "Derecho fundamental al habeas data y a la intimidad"),
    ("Ley 1581 de 2012", "Régimen general de protección de datos personales (estatutaria). Principios (art. 4), datos sensibles (art. 5-7), derechos (art. 8), deberes (arts. 17-18), sanciones (art. 23)"),
    ("Decreto 1074 de 2015, Libro 2, Parte 2, Título 2, Capítulo 25", "Compiló el Decreto 1377 de 2013: autorización, aviso de privacidad, política, transferencias, RNBD"),
    ("Ley 1266 de 2008, modificada por la Ley 2157 de 2021", "Habeas data financiero, crediticio y comercial; permanencia del dato negativo"),
    ("Ley 1273 de 2009", "Delitos informáticos: violación de datos personales (art. 269F)"),
    ("Circulares externas de la SIC", "RNBD, incidentes de seguridad, transferencias internacionales `[verificar versión vigente]`"),
    ("Sentencia C-748 de 2011", "Control previo de la Ley 1581; condicionamientos que siguen gobernando su interpretación `[verificar]`"),
  ],
  "autoridades": ["Superintendencia de Industria y Comercio — Delegatura para la Protección de Datos Personales",
                  "Superintendencia Financiera (dato financiero, en lo de su competencia)",
                  "Jueces de tutela (habeas data como derecho fundamental)"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta políticas, contratos y evidencias"),
    ("Correo", "Las respuestas a titulares se entregan como borrador"),
    ("Herramienta de anonimización", "Se pide al usuario anonimizar antes de compartir documentos con datos"),
  ],
  "mcp": ["drive", "box", "slack", "atlassian"],
  "cats": ["documentos", "regulatorio", "gestion"],
  "propias": [
    ("evaluacion-de-tratamiento", "Mapea la actividad de tratamiento, determina rol (responsable o encargado), base de legitimación, riesgos y obligaciones que se activan."),
    ("politica-y-aviso", "Redacta política de tratamiento y aviso de privacidad con el contenido mínimo del Decreto 1074, ajustados al tratamiento real."),
    ("atender-consulta-o-reclamo", "Procesa la consulta o el reclamo del titular dentro de los términos legales, con la respuesta y el registro de trazabilidad."),
    ("incidente-de-seguridad", "Ruta de respuesta a una violación de datos: contención, evaluación, reporte a la SIC y comunicación a titulares."),
    ("transferencia-internacional", "Evalúa si la operación es transferencia o transmisión, qué exige cada una y cómo se documenta."),
    ("habeas-data-financiero", "Aplica la Ley 1266 y la Ley 2157: permanencia del dato negativo, notificación previa al reporte y rutas de corrección."),
  ],
  "agentes": [("vigia-de-terminos-habeas-data", "Vigila los términos de consultas y reclamos de titulares y avisa antes de que venzan los 10 y 15 días hábiles.")],
  "decisiones": ["Postura sobre bases de legitimación distintas de la autorización",
                 "Umbral para reportar un incidente a la SIC",
                 "Política sobre uso de datos de clientes en herramientas de IA",
                 "Responsable interno del RNBD y de la atención de titulares"],
  "sensible": True,
 },
]

PLUGINS += [
 {
  "slug": "laboral-seguridad-social-co",
  "display": "Laboral y Seguridad Social",
  "desc": ("Resuelve el día a día laboral bajo el CST y la reforma de 2025: liquidación de "
           "prestaciones e indemnizaciones, terminación con y sin justa causa, procedimiento "
           "disciplinario con debido proceso, tipo de vinculación y riesgo de tercerización, "
           "acoso laboral bajo la Ley 1010 de 2006, riesgos laborales y accidentes de trabajo, y "
           "las rutas de pensión y seguridad social."),
  "ambito": "Derecho individual y colectivo del trabajo, seguridad social integral y riesgos laborales.",
  "normas": [
    ("Código Sustantivo del Trabajo (Decretos 2663 y 3743 de 1950)", "Contrato de trabajo, jornada, salario, prestaciones, terminación (art. 62-64), prescripción (art. 488)"),
    ("Ley 50 de 1990", "Cesantías con régimen anualizado, contrato a término fijo, salario integral"),
    ("Ley 789 de 2002", "Indemnización por despido sin justa causa (art. 28, que modificó el art. 64 CST)"),
    ("Ley 2466 de 2025", "Reforma laboral: contrato a término indefinido como regla, recargos, jornada y estabilidad `[verificar vigencia, reglamentación y transición]`"),
    ("Ley 2101 de 2021", "Reducción gradual de la jornada máxima legal"),
    ("Ley 2191 de 2022", "Desconexión laboral"),
    ("Ley 1010 de 2006", "Acoso laboral: conductas, comité de convivencia, procedimiento y caducidad de 6 meses"),
    ("Ley 100 de 1993 y Ley 797 de 2003", "Sistema general de pensiones, salud y riesgos"),
    ("Ley 1562 de 2012 y Decreto 1072 de 2015", "Riesgos laborales, SG-SST, accidente de trabajo y enfermedad laboral"),
    ("Ley 2381 de 2024", "Reforma pensional `[verificar estado de constitucionalidad, vigencia y régimen de transición]`"),
    ("Código Procesal del Trabajo y de la Seguridad Social", "Proceso ordinario laboral, competencia y prescripción (art. 151)"),
  ],
  "autoridades": ["Ministerio del Trabajo (inspección, vigilancia y control)", "Jueces laborales del circuito y municipales de pequeñas causas",
                  "Corte Suprema de Justicia, Sala de Casación Laboral", "UGPP (aportes)", "ARL, EPS y fondos de pensiones", "Juntas de Calificación de Invalidez"],
  "integraciones": [
    ("Sistema de nómina o HRIS", "El usuario aporta los datos salariales para cada liquidación"),
    ("Gestor documental", "El usuario adjunta contrato, descargos y soportes"),
    ("Correo", "Las comunicaciones al trabajador se entregan como borrador"),
  ],
  "mcp": ["drive", "box", "slack", "docusign"],
  "cats": ["documentos", "gestion", "firma"],
  "propias": [
    ("liquidar-prestaciones", "Liquida cesantías, intereses, prima, vacaciones, indemnizaciones y sanciones moratorias con memoria de cálculo y base salarial explícita."),
    ("terminacion-y-justa-causa", "Evalúa si la causal invocada se sostiene, qué hay que probar, qué procedimiento previo se exige y cuál es la exposición si el despido cae."),
    ("procedimiento-disciplinario", "Estructura descargos y decisión con debido proceso: citación, imputación clara, oportunidad de defensa y proporcionalidad."),
    ("vinculacion-y-tercerizacion", "Califica la relación real por encima de la forma y evalúa el riesgo de contrato realidad, intermediación ilegal y solidaridad."),
    ("acoso-laboral", "Ruta de la Ley 1010: comité de convivencia, medidas preventivas y correctivas, y control de la caducidad de seis meses."),
    ("riesgos-y-atel", "Accidente de trabajo y enfermedad laboral: calificación de origen, prestaciones, controversias ante junta y responsabilidad del empleador."),
  ],
  "agentes": [("vigia-laboral", "Vigila vencimientos laborales: contratos a término fijo por renovar, periodos de prueba, incapacidades prolongadas y términos de descargos.")],
  "decisiones": ["Postura frente a la terminación sin justa causa con indemnización",
                 "Umbral para escalar a abogado laboral externo",
                 "Política sobre estabilidad laboral reforzada y retiro del servicio",
                 "Criterio de la casa sobre transacciones y conciliaciones laborales"],
  "sensible": True,
 },
 {
  "slug": "societario-co",
  "display": "Societario",
  "desc": ("Acompaña la vida de la sociedad: elección de tipo societario y constitución de SAS, "
           "convocatoria y desarrollo de asambleas con actas que resistan impugnación, reformas "
           "estatutarias, deberes y responsabilidad de administradores bajo la Ley 222 de 1995, "
           "conflictos societarios ante la Superintendencia de Sociedades, y debida diligencia "
           "societaria para transacciones."),
  "ambito": "Derecho societario, gobierno corporativo y conflictos entre socios.",
  "normas": [
    ("Código de Comercio, Libro Segundo", "Sociedades comerciales: tipos, constitución, aportes, reformas, disolución y liquidación"),
    ("Ley 222 de 1995", "Deberes de administradores (art. 23), responsabilidad (art. 24), acción social de responsabilidad (art. 25), impugnación de decisiones (art. 191), grupos empresariales (arts. 26-31), derecho de inspección"),
    ("Ley 1258 de 2008", "Sociedad por Acciones Simplificada: libertad estatutaria, abuso del derecho de voto (art. 43), desestimación de la personalidad jurídica (art. 42), arbitraje societario"),
    ("Ley 1727 de 2014 y Decreto 1074 de 2015", "Registro mercantil y cámaras de comercio"),
    ("Ley 1901 de 2018", "Sociedades BIC"),
    ("Circular Básica Jurídica de la Superintendencia de Sociedades", "Doctrina vigente sobre gobierno, administradores y conflictos `[verificar versión]`"),
  ],
  "autoridades": ["Superintendencia de Sociedades (supervisión y facultades jurisdiccionales)",
                  "Cámaras de Comercio (registro mercantil)", "Tribunales de arbitramento (cláusulas compromisorias societarias)"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta estatutos, actas y certificados"),
    ("Firma electrónica", "Las actas se suscriben por fuera del plugin"),
    ("Cámara de comercio en línea", "El usuario aporta el certificado de existencia y representación"),
  ],
  "mcp": ["drive", "box", "docusign", "imanage"],
  "cats": ["documentos", "gobierno", "firma", "contratos"],
  "propias": [
    ("tipo-societario-y-constitucion", "Escoge el tipo societario por las razones correctas y arma el documento de constitución con los estatutos que el negocio necesita."),
    ("asamblea-y-actas", "Convocatoria, quórum, mayorías y acta redactada para resistir impugnación y para servir de prueba."),
    ("reforma-estatutaria", "Estructura la reforma con el procedimiento, las mayorías y el registro que exige cada tipo societario."),
    ("deberes-de-administradores", "Evalúa la actuación del administrador contra el art. 23 de la Ley 222, el conflicto de interés y la exposición a la acción social de responsabilidad."),
    ("conflicto-societario", "Mapea la vía para el conflicto entre socios: impugnación, acción social, abuso del derecho de voto, desestimación o arbitraje."),
  ],
  "agentes": [("vigia-societario", "Avisa los vencimientos societarios del año: reunión ordinaria de marzo, renovación de matrícula mercantil, informes y reportes a la Superintendencia.")],
  "decisiones": ["Postura sobre acuerdos de accionistas y su oponibilidad",
                 "Umbral de operaciones que requieren autorización de junta o asamblea",
                 "Política sobre conflicto de interés de administradores",
                 "Vía preferida de solución de controversias societarias"],
 },
 {
  "slug": "litigio-civil-co",
  "display": "Litigio Civil y Comercial",
  "desc": ("Lleva el proceso bajo el Código General del Proceso de punta a punta: competencia y "
           "viabilidad, demanda que no se inadmite, contestación con excepciones bien planteadas, "
           "plan probatorio, ejecutivo, medidas cautelares, recursos y cronología del caso. "
           "Controla términos con la norma a la vista y marca toda cita que no haya sido "
           "verificada en fuente oficial."),
  "ambito": "Proceso civil, comercial y de familia en la jurisdicción ordinaria; arbitraje.",
  "normas": [
    ("Ley 1564 de 2012", "Código General del Proceso: competencia (arts. 15-33), demanda (arts. 82-85), contestación (art. 96), excepciones previas (art. 100), pruebas (arts. 164-275), cautelares (arts. 590-604), verbal (arts. 368-373), verbal sumario (arts. 390-392), ejecutivo (arts. 422-472), recursos (arts. 318-355)"),
    ("Ley 2213 de 2022", "Actuaciones judiciales por medios electrónicos, poderes y notificaciones"),
    ("Ley 2220 de 2022", "Estatuto de Conciliación: requisito de procedibilidad `[verificar]`"),
    ("Ley 1563 de 2012", "Estatuto de Arbitraje Nacional e Internacional"),
    ("Código Civil y Código de Comercio", "Derecho sustancial que se hace valer en el proceso"),
    ("Sentencia C-157 de 2013", "Condicionamiento de la sanción por juramento estimatorio `[verificar]`"),
  ],
  "autoridades": ["Jueces civiles municipales, de pequeñas causas y del circuito", "Tribunales Superiores — Sala Civil",
                  "Corte Suprema de Justicia, Sala de Casación Civil", "Centros de arbitraje y conciliación"],
  "integraciones": [
    ("Consulta de procesos de la Rama Judicial", "El usuario aporta el estado del proceso"),
    ("Gestor documental", "El usuario adjunta las piezas del expediente"),
    ("Calendario", "Los términos se entregan en tabla, sin agendar"),
  ],
  "mcp": ["drive", "box", "imanage", "slack"],
  "cats": ["gestion", "documentos", "investigacion"],
  "propias": [
    ("viabilidad-y-competencia", "Antes de redactar: pretensión viable, juez competente, cuantía, trámite, caducidad o prescripción y requisito de procedibilidad."),
    ("redactar-demanda", "Demanda completa contra la lista del art. 82 del CGP, con hechos numerados, juramento estimatorio razonado y pruebas amarradas a cada hecho."),
    ("contestar-demanda", "Contestación con pronunciamiento hecho por hecho, excepciones de mérito estructuradas y objeción oportuna al juramento estimatorio."),
    ("plan-probatorio", "Convierte la teoría del caso en un plan de prueba: qué hay que probar, con qué medio, quién lo tiene y qué se pide al juez."),
    ("proceso-ejecutivo", "Verifica el título ejecutivo, arma el mandamiento de pago y anticipa las excepciones del ejecutado."),
    ("medidas-cautelares", "Escoge la cautelar procedente, sustenta apariencia de buen derecho y peligro en la demora, y calcula la caución."),
    ("recursos", "Escoge el recurso, controla la oportunidad y sustenta con reparos concretos, no con inconformidad genérica."),
    ("cronologia-del-caso", "Construye la línea de tiempo del expediente con fuente y folio de cada hecho, marcando lo que no está probado."),
  ],
  "agentes": [("vigia-terminos", "Revisa los procesos activos, cruza actuaciones y estados con los términos legales y avisa lo que vence, con la norma del término a la vista.")],
  "decisiones": ["Umbral de cuantía para asumir un litigio",
                 "Postura sobre medidas cautelares y cauciones",
                 "Política de sustentación de recursos y de casación",
                 "Criterio para recomendar conciliación o transacción"],
 },
 {
  "slug": "contencioso-administrativo-co",
  "display": "Contencioso Administrativo y Contratación Estatal",
  "desc": ("Trabaja frente al Estado bajo el CPACA: escoge el medio de control y controla la "
           "caducidad, agota vía gubernativa y conciliación prejudicial, arma nulidad y "
           "restablecimiento y reparación directa, redacta derechos de petición que obligan, "
           "sustenta apelaciones ante tribunal y Consejo de Estado, y maneja el ciclo de la "
           "contratación estatal bajo la Ley 80, la Ley 1150 y el Decreto 1082."),
  "ambito": "Derecho administrativo, contencioso administrativo y contratación estatal.",
  "normas": [
    ("Ley 1437 de 2011 (CPACA), modificada por la Ley 2080 de 2021", "Procedimiento administrativo, medios de control (art. 137 y ss.), caducidad (art. 164), extensión de jurisprudencia, recurso de unificación"),
    ("Ley 1755 de 2015", "Derecho de petición (sustituyó el Título II del CPACA)"),
    ("Ley 80 de 1993", "Estatuto General de Contratación de la Administración Pública"),
    ("Ley 1150 de 2007", "Modalidades de selección, riesgos, garantías, interventoría"),
    ("Decreto 1082 de 2015", "DUR del sector Planeación: reglamentación de la contratación estatal, SECOP"),
    ("Ley 2022 de 2020", "Documentos tipo obligatorios"),
    ("Ley 1474 de 2011", "Estatuto Anticorrupción: inhabilidades, supervisión e interventoría, responsabilidad fiscal"),
    ("Ley 610 de 2000", "Proceso de responsabilidad fiscal"),
    ("Ley 1952 de 2019, modificada por la Ley 2094 de 2021", "Código General Disciplinario"),
    ("Consejo de Estado, sentencias de unificación de 28 de agosto de 2014", "Topes de perjuicios inmateriales `[verificar]`"),
  ],
  "autoridades": ["Jueces y tribunales administrativos", "Consejo de Estado", "Procuraduría General de la Nación",
                  "Contraloría General de la República", "Agencia Nacional de Defensa Jurídica del Estado", "Colombia Compra Eficiente"],
  "integraciones": [
    ("SECOP II", "El usuario aporta el enlace o los documentos del proceso"),
    ("Gestor documental", "El usuario adjunta el acto administrativo y los antecedentes"),
    ("Correo", "Las peticiones se entregan como borrador"),
  ],
  "mcp": ["drive", "box", "imanage", "slack"],
  "cats": ["gestion", "documentos", "regulatorio"],
  "propias": [
    ("medio-de-control", "Escoge el medio de control correcto, fija la caducidad con su norma y define qué hay que agotar antes de demandar."),
    ("derecho-de-peticion", "Redacta la petición con objeto concreto, término aplicable y ruta cuando la autoridad no responde o responde mal."),
    ("nulidad-y-restablecimiento", "Ataca el acto administrativo por causal, con cargos separados y pretensión de restablecimiento cuantificada."),
    ("reparacion-directa", "Estructura la falla del servicio, el daño especial o el riesgo excepcional, con imputación y liquidación conforme a la unificación de 2014."),
    ("contratacion-estatal", "Acompaña el proceso de selección, la ejecución y la liquidación, con control de inhabilidades, riesgos y garantías."),
    ("apelacion-contenciosa", "Sustenta la apelación con reparos concretos, no con la repetición de la demanda."),
  ],
  "agentes": [("vigia-caducidad", "Vigila la caducidad de los medios de control en los asuntos abiertos y avisa con antelación suficiente para conciliar antes de demandar.")],
  "decisiones": ["Postura sobre conciliación prejudicial y comité de conciliación",
                 "Umbral para recomendar extensión de jurisprudencia frente a demanda",
                 "Política de defensa judicial y de acción de repetición",
                 "Criterio sobre contratación directa y sus riesgos"],
 },
 {
  "slug": "cumplimiento-co",
  "display": "Cumplimiento — SAGRILAFT, PTEE y Antisoborno",
  "desc": ("Determina qué régimen de cumplimiento obliga a la empresa y lo implementa: SAGRILAFT "
           "y PTEE bajo la Circular Básica Jurídica de la Superintendencia de Sociedades, "
           "responsabilidad administrativa por soborno transnacional de la Ley 1778 de 2016, "
           "debida diligencia de contrapartes, canal de denuncias y reporte a autoridades. "
           "Incluye la interacción con el régimen de datos personales."),
  "ambito": "Prevención de LA/FT/FPADM, transparencia y ética empresarial, antisoborno y anticorrupción privada.",
  "normas": [
    ("Circular Básica Jurídica de la Superintendencia de Sociedades — Capítulo X", "SAGRILAFT: sujetos obligados, factores de riesgo, debida diligencia, oficial de cumplimiento, reportes `[verificar circular externa vigente]`"),
    ("Circular Básica Jurídica — Capítulo XIII", "PTEE: Programas de Transparencia y Ética Empresarial `[verificar]`"),
    ("Ley 1778 de 2016", "Responsabilidad administrativa de personas jurídicas por soborno transnacional; competencia de la Superintendencia de Sociedades"),
    ("Ley 2195 de 2022", "Transparencia y prevención de la corrupción; responsabilidad administrativa de personas jurídicas; ampliación de programas de cumplimiento"),
    ("Ley 1474 de 2011", "Estatuto Anticorrupción"),
    ("Ley 599 de 2000", "Delitos de lavado de activos (art. 323), enriquecimiento ilícito, cohecho, soborno transnacional (art. 433)"),
    ("Estatuto Orgánico del Sistema Financiero y circulares de la SFC (SARLAFT)", "Para entidades vigiladas por la Superintendencia Financiera"),
    ("Ley 1581 de 2012", "Límite al tratamiento de datos en la debida diligencia y en las investigaciones internas"),
  ],
  "autoridades": ["Superintendencia de Sociedades", "Superintendencia Financiera", "UIAF (reportes ROS)",
                  "Fiscalía General de la Nación", "Superintendencias sectoriales con régimen propio"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta manuales, matrices y evidencias"),
    ("Listas restrictivas y verificación de contrapartes", "La verificación se hace por fuera y el usuario aporta el resultado"),
    ("Canal de denuncias", "Los casos se cargan manualmente"),
  ],
  "mcp": ["drive", "box", "slack", "atlassian"],
  "cats": ["regulatorio", "documentos", "gestion"],
  "propias": [
    ("diagnostico-de-obligados", "Determina si la empresa es sujeto obligado a SAGRILAFT, a PTEE, a ambos o a ninguno, con los umbrales y el año de corte."),
    ("sagrilaft", "Estructura o audita el sistema: matriz de riesgo, segmentación, debida diligencia, señales de alerta, oficial de cumplimiento y reportes."),
    ("ptee", "Diseña o revisa el Programa de Transparencia y Ética Empresarial y su articulación con el gobierno corporativo."),
    ("debida-diligencia-de-contraparte", "Aplica debida diligencia simplificada, normal o intensificada según el riesgo, respetando el régimen de datos personales."),
    ("canal-de-denuncias", "Diseña el canal y el protocolo de investigación interna con debido proceso y protección al denunciante."),
  ],
  "agentes": [("vigia-de-cumplimiento", "Avisa los vencimientos del calendario de cumplimiento: informes del oficial, capacitaciones, actualización de matrices y reportes a la Superintendencia.")],
  "decisiones": ["Umbral de riesgo para debida diligencia intensificada",
                 "Postura sobre operaciones con jurisdicciones de alto riesgo",
                 "Quién decide un reporte de operación sospechosa",
                 "Política sobre investigaciones internas y participación de abogado externo"],
  "sensible": True,
 },
 {
  "slug": "tributario-co",
  "display": "Tributario",
  "desc": ("Trabaja el procedimiento y el riesgo tributario bajo el Estatuto Tributario: revisión "
           "de declaraciones y correcciones, respuesta a requerimientos especiales y pliegos, "
           "recurso de reconsideración, procedimiento administrativo de cobro coactivo, "
           "obligaciones formales y facturación electrónica, y análisis de riesgo de posiciones "
           "fiscales antes de tomarlas."),
  "ambito": "Procedimiento tributario nacional y territorial, obligaciones formales y contingencias fiscales.",
  "normas": [
    ("Estatuto Tributario (Decreto 624 de 1989)", "Procedimiento: firmeza (art. 714), requerimiento especial (arts. 703-707), liquidación de revisión (art. 710), recurso de reconsideración (art. 720), sanciones (arts. 634 y ss.), cobro coactivo (arts. 823 y ss.)"),
    ("Ley 2277 de 2022", "Reforma tributaria para la igualdad y la justicia social `[verificar artículos declarados inexequibles]`"),
    ("Ley 2010 de 2019", "Ley de crecimiento económico; reexpidió buena parte de la Ley 1943 de 2018"),
    ("Sentencia C-481 de 2019", "Inexequibilidad de la Ley 1943 de 2018 por vicios de trámite, con efectos diferidos `[verificar]`"),
    ("Decreto 1625 de 2016", "DUR en materia tributaria"),
    ("Ley 1437 de 2011", "CPACA: control judicial de los actos de la DIAN"),
    ("Resoluciones de la DIAN", "Facturación electrónica, UVT, plazos y formularios `[verificar año]`"),
  ],
  "autoridades": ["DIAN", "Secretarías de Hacienda departamentales y municipales",
                  "Jueces y tribunales administrativos", "Consejo de Estado, Sección Cuarta"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta declaraciones, actos y soportes"),
    ("Sistema contable", "El usuario aporta cifras y conciliaciones"),
  ],
  "mcp": ["drive", "box", "slack"],
  "cats": ["documentos", "regulatorio", "gestion"],
  "propias": [
    ("revision-de-declaracion", "Revisa la declaración contra el soporte, identifica inconsistencias y decide entre corrección voluntaria, provocada o defensa."),
    ("respuesta-a-requerimiento", "Responde el requerimiento especial o el emplazamiento dentro del término, con prueba y con la discusión jurídica que después sostiene el recurso."),
    ("recurso-de-reconsideracion", "Sustenta el recurso preservando los cargos para la eventual demanda de nulidad y restablecimiento."),
    ("cobro-coactivo", "Ruta frente al mandamiento de pago: excepciones, facilidades de pago, medidas cautelares y prescripción de la acción de cobro."),
    ("riesgo-de-posicion-fiscal", "Evalúa una posición antes de tomarla: soporte normativo, doctrina de la DIAN, jurisprudencia y exposición sancionatoria."),
  ],
  "agentes": [("vigia-tributario", "Avisa vencimientos de calendario tributario, términos de respuesta a requerimientos y fechas de firmeza de las declaraciones.")],
  "decisiones": ["Apetito de riesgo frente a posiciones fiscales agresivas",
                 "Umbral para pedir concepto a la DIAN o a asesor externo",
                 "Política sobre corrección voluntaria frente a defensa",
                 "Criterio para provisionar contingencias fiscales"],
 },
]

PLUGINS += [
 {
  "slug": "propiedad-intelectual-co",
  "display": "Propiedad Intelectual",
  "desc": ("Gestiona la propiedad intelectual bajo el régimen andino y la ley colombiana: "
           "viabilidad y registro de marca ante la SIC con análisis de confundibilidad, "
           "oposiciones y cancelaciones, derecho de autor y registro de software ante la DNDA, "
           "contratos de licencia y cesión, acciones por infracción y competencia desleal, y "
           "control de vencimientos de la cartera."),
  "ambito": "Propiedad industrial (marcas, patentes, diseños), derecho de autor y derechos conexos, secretos empresariales.",
  "normas": [
    ("Decisión Andina 486 de 2000", "Régimen común de propiedad industrial: marcas (arts. 134-189), patentes, diseños, secretos empresariales, acciones por infracción (arts. 238 y ss.)"),
    ("Decisión Andina 351 de 1993", "Régimen común de derecho de autor y derechos conexos"),
    ("Ley 23 de 1982", "Derecho de autor en Colombia"),
    ("Ley 1915 de 2018", "Modernización del derecho de autor: excepciones, medidas tecnológicas, indemnizaciones preestablecidas"),
    ("Ley 256 de 1996", "Competencia desleal, incluida la explotación de la reputación ajena y la violación de secretos"),
    ("Ley 1564 de 2012", "CGP: proceso verbal para infracción; facultades jurisdiccionales de la SIC"),
    ("Circular Única de la SIC — Título X", "Trámites de propiedad industrial `[verificar versión vigente]`"),
  ],
  "autoridades": ["Superintendencia de Industria y Comercio — Delegatura para la Propiedad Industrial",
                  "Dirección Nacional de Derecho de Autor (DNDA)", "Tribunal de Justicia de la Comunidad Andina (interpretación prejudicial)",
                  "Jueces civiles del circuito y SIC en función jurisdiccional"],
  "integraciones": [
    ("Gestor documental", "El usuario adjunta certificados, publicaciones y evidencias de uso"),
    ("Base de datos de marcas de la SIC", "La búsqueda de antecedentes la hace el usuario y aporta el resultado"),
    ("Calendario", "Los vencimientos se entregan en tabla"),
  ],
  "mcp": ["drive", "box", "docusign", "slack"],
  "cats": ["pi", "documentos", "contratos"],
  "propias": [
    ("viabilidad-de-marca", "Analiza distintividad, causales absolutas y relativas y riesgo de confusión antes de gastar en un registro que se va a negar."),
    ("oposicion-y-cancelacion", "Arma la oposición o la cancelación por no uso con la carga probatoria que exige la Decisión 486."),
    ("derecho-de-autor-y-software", "Determina titularidad, obra por encargo y relación laboral, y arma el registro ante la DNDA."),
    ("contratos-de-pi", "Licencia, cesión y desarrollo: qué se transfiere, qué no se puede transferir y qué exige el registro para ser oponible."),
    ("infraccion-y-cese", "Evalúa la infracción, redacta el requerimiento de cese y define la vía y las cautelares."),
  ],
  "agentes": [("vigia-de-cartera-pi", "Vigila vencimientos de renovación de marcas, anualidades de patentes y plazos de oposición y de prueba de uso.")],
  "decisiones": ["Umbral para presentar oposición frente a coexistir",
                 "Política de renovación de marcas sin uso",
                 "Postura sobre requerimientos de cese antes de demandar"],
 },
 {
  "slug": "regulatorio-co",
  "display": "Regulatorio y Vigilancia Normativa",
  "desc": ("Mantiene al equipo al día con lo que se publica y con lo que decide la jurisprudencia: "
           "vigilancia del Diario Oficial, de las superintendencias y de las altas cortes, "
           "análisis de impacto de una norma nueva sobre las obligaciones vigentes, comentarios a "
           "proyectos normativos en consulta pública, mapa de obligaciones por área, y el boletín "
           "que el equipo sí lee el lunes."),
  "ambito": "Vigilancia normativa y jurisprudencial, análisis de impacto regulatorio y gestión de obligaciones.",
  "normas": [
    ("Ley 1437 de 2011, art. 8", "Deber de publicidad y consulta de proyectos de regulación"),
    ("Decreto 1081 de 2015", "DUR de la Presidencia: publicidad de proyectos de actos administrativos"),
    ("Ley 1712 de 2014", "Transparencia y acceso a la información pública"),
    ("Ley 153 de 1887, arts. 71-72", "Derogatoria expresa, orgánica y tácita"),
    ("Constitución Política, arts. 241 y 243", "Control de constitucionalidad y cosa juzgada constitucional"),
  ],
  "autoridades": ["Imprenta Nacional — Diario Oficial", "Superintendencias sectoriales", "Ministerios y unidades administrativas especiales",
                  "Corte Constitucional, Corte Suprema y Consejo de Estado", "Departamento Administrativo de la Función Pública"],
  "integraciones": [
    ("Correo y calendario", "El boletín se entrega en línea"),
    ("Canal de equipo", "El digest se publica manualmente"),
    ("Gestor documental", "El mapa de obligaciones se guarda por fuera"),
  ],
  "mcp": ["drive", "slack", "atlassian", "asana"],
  "cats": ["regulatorio", "gestion", "correo"],
  "propias": [
    ("vigilancia-normativa", "Barrido periódico de fuentes oficiales con filtro de materialidad, para que el equipo lea diez líneas y no doscientas."),
    ("analisis-de-impacto", "Toma una norma nueva y dice qué cambia en las obligaciones, en los contratos y en los procesos de la organización."),
    ("comentarios-a-proyecto", "Redacta comentarios a un proyecto en consulta pública con argumento técnico y propuesta de texto."),
    ("mapa-de-obligaciones", "Construye y mantiene la matriz de obligaciones normativas por área, con responsable y evidencia."),
    ("boletin-normativo", "Arma el boletín periódico con novedades priorizadas y acción concreta por cada una."),
  ],
  "agentes": [("vigia-normativo", "Corre la vigilancia en la periodicidad configurada, filtra por materialidad y entrega el digest listo para publicar.")],
  "decisiones": ["Fuentes y periodicidad de la vigilancia",
                 "Criterio de materialidad para que una novedad entre al boletín",
                 "Destinatarios del boletín y formato"],
 },
 {
  "slug": "gobernanza-ia-co",
  "display": "Gobernanza de Inteligencia Artificial",
  "desc": ("Gobierna el uso de IA en la organización y en la práctica jurídica desde el marco "
           "colombiano: inventario de sistemas, triage de casos de uso por riesgo, evaluación de "
           "impacto que cruza protección de datos y derechos fundamentales, política interna de "
           "uso de IA, revisión de contratos con proveedores de IA, y las reglas de uso de IA "
           "generativa en actuaciones judiciales."),
  "ambito": "Gobernanza, riesgo y cumplimiento de sistemas de inteligencia artificial en Colombia.",
  "normas": [
    ("Constitución Política, arts. 15, 20 y 29", "Habeas data, información y debido proceso frente a decisiones automatizadas"),
    ("Ley 1581 de 2012 y Decreto 1074 de 2015", "Tratamiento de datos personales en sistemas de IA; principios de finalidad, necesidad y calidad del dato"),
    ("Ley 1712 de 2014", "Transparencia y acceso a la información pública, aplicable a IA en el sector público"),
    ("Ley 2213 de 2022", "Uso de TIC en actuaciones judiciales"),
    ("Ley 1123 de 2007", "Deberes de diligencia, lealtad y reserva del abogado que usa herramientas de IA"),
    ("CONPES de política nacional de inteligencia artificial", "Lineamientos de política pública `[verificar número, fecha y vigencia]`"),
    ("Lineamientos del Consejo Superior de la Judicatura sobre IA en la Rama Judicial", "`[verificar acuerdo o circular vigente]`"),
    ("Ley 1480 de 2011", "Información al consumidor cuando la IA interviene en la relación de consumo"),
  ],
  "autoridades": ["Superintendencia de Industria y Comercio (datos personales y consumidor)",
                  "Ministerio de Ciencia, Tecnología e Innovación y MinTIC", "Consejo Superior de la Judicatura",
                  "Superintendencias sectoriales según el uso"],
  "integraciones": [
    ("Gestor documental", "El inventario y las evaluaciones se guardan por fuera"),
    ("Gestor de tareas", "Los hallazgos se cargan manualmente"),
  ],
  "mcp": ["drive", "box", "atlassian", "linear", "slack"],
  "cats": ["regulatorio", "gestion", "documentos"],
  "propias": [
    ("inventario-de-ia", "Levanta y mantiene el inventario de sistemas de IA con propósito, datos, proveedor, decisiones que afecta y responsable."),
    ("triage-de-caso-de-uso", "Clasifica un caso de uso propuesto por riesgo y decide qué controles y qué aprobaciones se activan."),
    ("evaluacion-de-impacto-ia", "Evaluación de impacto que cruza el régimen de datos personales con los derechos fundamentales que el sistema puede afectar."),
    ("politica-de-uso-de-ia", "Redacta la política interna: usos permitidos, prohibidos, revisión humana obligatoria y régimen de datos."),
    ("revision-de-proveedor-ia", "Revisa el contrato del proveedor: entrenamiento con datos del cliente, subencargados, transferencias, auditoría y responsabilidad."),
    ("ia-en-la-practica-juridica", "Reglas de uso de IA en piezas que se radican: verificación de citas, transparencia frente al despacho y reserva profesional."),
  ],
  "agentes": [],
  "decisiones": ["Quién aprueba un nuevo caso de uso de IA",
                 "Usos prohibidos sin excepción",
                 "Regla de revisión humana obligatoria",
                 "Postura sobre datos de clientes en herramientas de terceros"],
  "sensible": True,
 },
 {
  "slug": "estudiante-derecho-co",
  "display": "Estudiante de Derecho",
  "desc": ("Acompaña el estudio del Derecho colombiano sin hacer la tarea: ficha sentencias "
           "separando ratio de obiter, interroga con método socrático, enseña a construir líneas "
           "jurisprudenciales, prepara exámenes y preparatorios por materia, y corrige escritura "
           "jurídica exigiendo estructura y cita correcta."),
  "ambito": "Formación jurídica de pregrado y preparación de exámenes preparatorios.",
  "normas": [
    ("Constitución Política de 1991", "Base del estudio de todas las materias"),
    ("Ley 169 de 1896, art. 4", "Doctrina probable"),
    ("Ley 270 de 1996", "Estatutaria de administración de justicia"),
    ("Códigos vigentes", "CC, C.Co., CST, CP, CPP, CGP, CPACA, ET"),
    ("Sentencias hito", "Ver `referencias/precedente-y-jurisprudencia.md`"),
  ],
  "autoridades": ["Corte Constitucional", "Corte Suprema de Justicia", "Consejo de Estado", "Universidad y programa académico"],
  "integraciones": [
    ("Gestor documental", "El estudiante adjunta las sentencias y lecturas"),
    ("Calendario", "El plan de estudio se entrega en tabla"),
  ],
  "mcp": ["drive", "slack"],
  "cats": ["investigacion", "documentos"],
  "propias": [
    ("ficha-de-sentencia", "Ficha la sentencia con problema jurídico, ratio, obiter, decisum, salvamentos y ubicación en la línea."),
    ("metodo-socratico", "Interroga sobre la lectura hasta que la respuesta se sostenga; no entrega la respuesta hecha."),
    ("construir-linea-jurisprudencial", "Enseña el método completo: sentencia arquimédica, nicho citacional, patrón de sombra y puntos de quiebre."),
    ("preparacion-de-examen", "Arma el plan por materia con los temas que efectivamente se preguntan y ejercicios de aplicación."),
    ("escritura-juridica", "Corrige el escrito exigiendo estructura, precisión y cita verificable, y explica cada corrección."),
  ],
  "agentes": [],
  "decisiones": ["Materias y semestre en curso",
                 "Universidad y método de evaluación predominante",
                 "Fecha del preparatorio o del examen objetivo"],
  "no_hace": ["Escribir el trabajo, el ensayo o el parcial por el estudiante",
              "Entregar respuestas de examen",
              "Resolver el caso sin que el estudiante haya intentado la respuesta primero"],
 },
 {
  "slug": "consultorio-juridico-co",
  "display": "Consultorio Jurídico",
  "desc": ("Sostiene la operación del consultorio jurídico universitario bajo la Ley 2113 de 2021: "
           "entrevista y ficha de consulta, concepto para el usuario en lenguaje claro, control de "
           "términos con criterio de prevención del daño, cola de revisión del docente antes de "
           "que salga cualquier pieza, y entrega ordenada de casos al final del semestre."),
  "ambito": "Consultorios jurídicos y centros de conciliación universitarios; asistencia jurídica gratuita.",
  "normas": [
    ("Ley 2113 de 2021", "Consultorios jurídicos: naturaleza, funciones, competencias y supervisión docente"),
    ("Decreto 196 de 1971 y Ley 1123 de 2007", "Ejercicio de la abogacía y régimen disciplinario aplicable a quien supervisa"),
    ("Ley 1564 de 2012", "CGP: amparo de pobreza, representación y competencias"),
    ("Ley 2220 de 2022", "Conciliación en centros universitarios `[verificar]`"),
    ("Ley 1581 de 2012", "Protección de datos de los usuarios del consultorio"),
  ],
  "autoridades": ["Universidad y su facultad de Derecho", "Consejo Superior de la Judicatura (registro de consultorios)",
                  "Ministerio de Justicia (centros de conciliación)", "Jueces y autoridades ante quienes actúa el consultorio"],
  "integraciones": [
    ("Gestor documental", "Las fichas y conceptos se guardan en la carpeta del consultorio"),
    ("Calendario", "Los términos se entregan en tabla"),
  ],
  "mcp": ["drive", "slack"],
  "cats": ["gestion", "documentos"],
  "propias": [
    ("entrevista-de-consulta", "Guía la entrevista para levantar los hechos completos, identificar el problema jurídico y detectar términos que corran."),
    ("concepto-para-usuario", "Redacta el concepto en lenguaje claro, con la ruta, los términos y lo que el usuario debe hacer y aportar."),
    ("control-de-terminos", "Lleva el tablero de términos del consultorio con criterio de prevención del daño al usuario."),
    ("cola-de-revision-docente", "Ninguna pieza sale sin revisión: arma la cola con lo que el docente necesita para revisar rápido."),
    ("entrega-de-semestre", "Prepara la entrega de casos al siguiente estudiante con todo lo que hay que saber para no perder un término."),
  ],
  "agentes": [("vigia-de-consultorio", "Revisa la cola de casos y avisa términos próximos y piezas pendientes de revisión docente.")],
  "decisiones": ["Alcance de la representación que asume el consultorio",
                 "Quién es el docente responsable de cada área",
                 "Regla de rechazo de casos fuera de competencia",
                 "Protocolo de entrega al final del semestre"],
  "sensible": True,
 },
 {
  "slug": "hub-constructor-legal-co",
  "display": "Hub de Constructores Legales",
  "desc": ("Encuentra, evalúa, instala y mantiene skills jurídicas de la comunidad colombiana con "
           "una compuerta de revisión de seguridad y de calidad jurídica antes de que algo entre "
           "al entorno. Incluye un creador de skills que impone las convenciones de este "
           "repositorio: verificación de fuentes, control de términos y compuertas de revisión "
           "profesional."),
  "ambito": "Gestión del ecosistema de skills jurídicas: descubrimiento, revisión, instalación y control de calidad.",
  "normas": [
    ("Ley 1123 de 2007", "Los deberes profesionales viajan con la herramienta: una skill mal hecha no exonera al abogado"),
    ("Ley 1581 de 2012", "Ninguna skill instalada puede exfiltrar datos de clientes"),
    ("Ley 1273 de 2009", "Delitos informáticos: acceso abusivo y uso de software malicioso"),
  ],
  "autoridades": ["No aplica — control interno del entorno"],
  "integraciones": [
    ("Repositorios de skills", "El usuario aporta el enlace del repositorio a evaluar"),
    ("Gestor documental", "El registro de skills instaladas se guarda por fuera"),
  ],
  "mcp": ["drive", "slack", "atlassian"],
  "cats": ["gestion", "documentos"],
  "propias": [
    ("explorar-registro", "Busca skills jurídicas colombianas en los registros configurados y las resume con su procedencia y su frescura."),
    ("revisar-seguridad", "Compuerta obligatoria: revisa la skill antes de instalarla — permisos, comandos, exfiltración, dependencias y calidad jurídica."),
    ("instalar-skill", "Instala solo lo que pasó la revisión, deja registro y explica qué quedó habilitado."),
    ("crear-skill-juridica", "Crea una skill nueva con las convenciones del repositorio: frontmatter, verificación de fuentes, compuertas y salidas."),
    ("control-de-calidad", "Audita las skills instaladas contra la lista de calidad: citas, términos, compuertas y actualidad normativa."),
  ],
  "agentes": [],
  "decisiones": ["Lista de registros permitidos",
                 "Quién autoriza una instalación",
                 "Frecuencia de la auditoría de calidad"],
 },
]
