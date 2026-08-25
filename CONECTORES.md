# Conectores

Qué se puede conectar a estos plugins, qué falta por construir en Colombia, y cómo
decidir si vale la pena.

## Conectores genéricos que ya funcionan

Los `.mcp.json` de los plugins sugieren servidores MCP de proveedores que no dependen
de la jurisdicción:

| Conector | Para qué sirve aquí |
|---|---|
| **Google Drive** / **Box** | Traer el expediente, las minutas de la casa, los soportes |
| **iManage** | Gestión documental jurídica con control de acceso |
| **Slack** | Publicar alertas de términos y boletines normativos |
| **DocuSign** | Estado de firma de contratos y actas |
| **Atlassian** / **Asana** / **Linear** | Seguimiento de hallazgos y de tareas de cumplimiento |

Instalarlos no es automático: cada uno requiere autorización del usuario. En una sesión
interactiva, `/mcp`; desde la terminal, `claude mcp`.

## Lo que en Colombia todavía no tiene conector — y sí lo necesita

Esta es la brecha real. Ninguna de estas fuentes expone hoy un MCP oficial:

| Fuente | Qué desbloquearía | Dificultad |
|---|---|---|
| **SUIN-Juriscol** | Verificación de vigencia normativa automática. Es la pieza que más valor agregaría a todo el repositorio | Media — el sitio expone búsqueda pero no API pública documentada |
| **Relatoría de la Corte Constitucional** | Verificar existencia de sentencias y traer la *ratio* | Media |
| **Relatorías de la Corte Suprema y del Consejo de Estado** | Ídem, con la nomenclatura moderna (`SC1234-2023`) | Media |
| **Rama Judicial — consulta de procesos y estados** | Vigía de términos con datos reales del expediente | Alta — captcha y sesiones |
| **SECOP II** | Seguimiento de procesos de contratación estatal | Media — hay datos abiertos |
| **Diario Oficial** | Vigilancia normativa diaria automática | Media |
| **RUES / cámaras de comercio** | Existencia y representación, verificación de contrapartes | Alta — es de pago |
| **SIC — bases de marcas y de RNBD** | Antecedentes marcarios y verificación de registro | Media |
| **DIAN** | Conceptos, calendario tributario, UVT vigente | Media |
| **Datos abiertos (datos.gov.co)** | Varias de las anteriores por vía indirecta | Baja |

**Mientras tanto**, las skills funcionan pidiendo al usuario que aporte la fuente y
marcando `[conocimiento del modelo — verificar]` todo lo que no se recuperó. Eso es
deliberado: es mejor que un conector inexistente y una cita inventada.

## Conectores propios

Si su firma ya tiene un servidor MCP —de jurisprudencia, de gestión de casos, de
anonimización— configúrelo a nivel de usuario y las skills lo usarán. El chequeo previo
de cada skill detecta si un conector de investigación está respondiendo y lo registra
en la línea **Fuentes:** de la nota al revisor.

Para construir uno: la skill `crear-skill-juridica` del plugin
`hub-constructor-legal-co` y la documentación de MCP de Anthropic.

## Regla de seguridad para conectores de terceros

Antes de instalar un conector jurídico de la comunidad, pase por
`/hub-constructor-legal-co:revisar-seguridad`. Un conector con acceso a su gestor
documental tiene acceso a expedientes de clientes bajo reserva profesional. La
compuerta existe por eso.

Preguntas mínimas antes de conectar algo:

1. ¿Quién lo opera y bajo qué contrato?
2. ¿Los documentos salen de su infraestructura? ¿A qué país?
3. ¿Se usan sus datos para entrenar modelos?
4. ¿Hay contrato de transmisión de datos con las cláusulas del art. 25 del
   Decreto 1074 de 2015?
5. Si hay transferencia internacional, ¿el país tiene nivel adecuado según la SIC, o
   aplica alguna excepción del art. 26 de la Ley 1581 de 2012?

Ver `referencias/tratamiento-de-datos.md`.
